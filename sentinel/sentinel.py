# -*- coding: utf-8 -*-
"""Sentinel Tools for Sentinel Satellites

 Sentinel Tools - Sentinel Satellites
======================================
 Super class for the Sentinel classes

 This file is a part of Sentinel Tools

 Copyright 2020 - MET Norway (Machine Ocean Project)

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import logging
import json

from os import path
from datetime import datetime, timezone
from enum import Enum

from .config import Config
from .autoapi import AutoAPI
from .tools import ensureFolderExists, isValidUUID4

logger = logging.getLogger(__name__)

class Sentinel():

    DIR_QUERY = "QueryData"
    DIR_STATE = "QueryState"
    IDX_DATA  = "dataIndex.json"

    def __init__(self, confOrAPI, dataPath=None):

        if isinstance(confOrAPI, AutoAPI):
            self._theAPI = confOrAPI.getAPI()
            self._theConfig = confOrAPI.getConfig()
        elif isinstance(confOrAPI, Config):
            self._theAPI = AutoAPI(confOrAPI).getAPI()
            self._theConfig = confOrAPI
        else:
            raise AttributeError(
                "confOrAPI must be either a Config or an AutoAPI object, got %s" % type(confOrAPI)
            )

        if dataPath is None:
            self._dataPath = self._theConfig.dataPath
        else:
            self._dataPath = dataPath

        if not path.isdir(self._dataPath):
            logger.error("Data folder does not exist: %s" % dataPath)
            raise FileNotFoundError("Data folder does not exist: %s" % dataPath)

        self._queryDir = path.join(self._dataPath, self.DIR_QUERY)
        self._stateDir = path.join(self._dataPath, self.DIR_STATE)
        self._indexPath = path.join(self._dataPath, self.IDX_DATA)

        self._dataIndex = {}
        self._indexChanged = False

        # self._loadDataIndex()

        return

    ##
    #  Getters
    ##

    @property
    def dataPath(self):
        return self._dataPath

    ##
    #  Setters
    ##

    @dataPath.setter
    def dataPath(self, value):
        if isinstance(value, str):
            self._dataPath = value
        else:
            logger.error("Parameter 'value' must be a string")
            raise ValueError("Parameter 'value' must be a string")
        return

    def _logQueryEntry(self, uuid, title=None, date=None, size=None, status=None):
        """Set the values for a dataset in the index.
        """
        newEntry = self._dataIndex.get(uuid, {
            "title": "",
            "date": "",
            "size": "",
            "status": DataSetStatus.NEW.name,
        })
        if title is not None:
            newEntry["title"] = str(title)
        if date is not None:
            newEntry["date"] = str(date)
        if size is not None:
            newEntry["size"] = str(size)
        if status is not None:
            if isinstance(status, DataSetStatus):
                newEntry["status"] = status.name
            else:
                raise AttributeError(
                    "status is of type %s, expected enum DataSetStatus" % type(status)
                )
        self._dataIndex[uuid] = newEntry
        self._indexChanged = True
        return

    ##
    #  Methods
    ##

    def processSearch(self, searchName, contLast=False, endPosition=None, saveResult=True):
        """Process a saved search from the main config file and
        optionally continue from the last point until now or a given
        end position.
        """
        theSearch = self._theConfig.getSearch(searchName)
        if not theSearch:
            logger.error("No saved search named '%s'" % searchName)
            return {}

        logger.info("Processing search: %s" % searchName)

        qArea = None
        qRaw = None
        qAreaRelation = "Intersects"
        startFrom = None
        kwArgs = {}
        for aKey, aValue in theSearch.items():
            if aKey == "area":
                qArea = aValue
            elif aKey == "raw":
                qRaw = aValue
            elif aKey == "area_relation":
                qAreaRelation = aValue
            elif aKey == "startfrom":
                startFrom = aValue
            else:
                kwArgs[aKey] = aValue

        if startFrom is not None:
            if endPosition is None:
                qDate = (startFrom, "NOW")
            else:
                qDate = (startFrom, endPosition)
        else:
            qDate = None

        theQuery = self._theAPI.format_query(
            area=qArea, date=qDate, raw=qRaw, area_relation=qAreaRelation, **kwArgs
        )
        logger.info("Processing Query: %s" % theQuery)
        qDict = self._theAPI.query(raw=theQuery)

        if saveResult:
            self.saveQueryResults(qDict)

        return qDict

    def saveQueryResults(self, qDict):
        """Split up a query result and save it to the data folder.
        """
        ensureFolderExists(self._queryDir)
        nSaved = 0
        for qUUID, qData in qDict.items():
            if not isValidUUID4(qUUID):
                logger.warning("Entry %s: Invalid" % qUUID)
                continue

            cleanDict = {}
            for aKey, aValue in qData.items():
                if isinstance(aValue, str):
                    cleanDict[aKey] = aValue
                elif isinstance(aValue, int):
                    cleanDict[aKey] = aValue
                elif isinstance(aValue, float):
                    cleanDict[aKey] = aValue
                elif isinstance(aValue, bool):
                    cleanDict[aKey] = aValue
                elif isinstance(aValue, datetime):
                    cleanDict[aKey] = aValue.isoformat(sep="T", timespec="milliseconds")+"Z"
                else:
                    logger.error("Unsupported datatype %s of key '%s'" % (type(aValue), aKey))

            entryDir = path.join(self._queryDir, qUUID[:2])
            ensureFolderExists(entryDir)

            entryFile = path.join(entryDir, qUUID+".json")
            try:
                with open(entryFile, mode="w+", encoding="utf8") as outFile:
                    outFile.write(json.dumps(cleanDict, indent=2))
                logger.info("Entry %s: Saved" % qUUID)
                if "summary" in cleanDict:
                    logger.info("> %s" % cleanDict["summary"])
            except Exception as e:
                logger.error("Failed to save entry %s" % qUUID)
                logger.error(str(e))
                continue

            # self.setIndexEntry(
            #     uuid=qUUID,
            #     title=cleanDict.get("title", None),
            #     size=cleanDict.get("size", None),
            #     date=cleanDict.get("beginposition", None)
            # )
            nSaved += 1

        return nSaved

    def flushIndex(self):
        """Save the index to file.
        """
        if self._indexChanged:
            self._flushDataIndex()
            self._indexChanged = False
            logger.debug("Data index flushed")
        return

    ##
    #  Internal Functions
    ##

    def _loadDataIndex(self):
        """Load the index of known datasets.
        """
        self._dataIndex = {}
        if path.isfile(self._indexPath):
            try:
                with open(self._indexPath, mode="r", encoding="utf8") as inFile:
                    theData = inFile.read()
                self._dataIndex = json.loads(theData)
            except Exception as e:
                logger.error("Failed to load data index")
                logger.error(str(e))
                return False
        else:
            logger.info("No previous data index found")
        return True

    def _flushDataIndex(self):
        """Save the data index to file.
        """
        try:
            with open(self._indexPath, mode="w+", encoding="utf8") as outFile:
                outFile.write(json.dumps(self._dataIndex, indent=2))
        except Exception as e:
            logger.error("Failed to save data index")
            logger.error(str(e))
            return False
        return True

# END Class Sentinel

class DataSetStatus(Enum):

    NONE = 0
    NEW = 1
    DOWNLOADED = 2
    MISSING = 3

# END Class DataSetStatus
