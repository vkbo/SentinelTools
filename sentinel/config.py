# -*- coding: utf-8 -*-
"""Sentinel Tools Config Class

 Sentinel Tools - Config Class
===============================
 Config class for the Machine Ocean Toolbox

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

import sys
import json
import logging

from os import path

logger = logging.getLogger(__name__)

class Config():

    def __init__(self, lookFolder=None):

        self._packRoot = None
        self._lookFolder = lookFolder
        self._confPath = None

        # Config Settings
        self.apiUser = ""
        self.apiPass = ""
        self.apiURL  = ""

        self._loadConfig()

        return

    def __str__(self):
        """Return a string of the content of the class.
        """
        return (
            "API Username: {apiUser:s}\n"
            "API Password: {apiPass:s}\n"
            "API URL:      {apiURL:s}\n"
        ).format(
            apiUser = self.apiUser,
            apiPass = "*"*len(self.apiPass),
            apiURL  = self.apiURL,
        )

    def printInfo(self, showPw=False):
        """Print the settings to the logger.
        """
        apiPass = self.apiPass if showPw else "*"*len(self.apiPass)
        logger.info("API Username: %s" % self.apiUser)
        logger.info("API Password: %s" % apiPass)
        logger.info("API URL:      %s" % self.apiURL)
        return

    ##
    #  Internal Functions
    ##

    def _loadConfig(self):
        """Load the config files, if they exist, and extract the data.
        """
        self._packRoot = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
        rootDir = path.abspath(path.join(self._packRoot, path.pardir))
        logger.debug("Package root directory is: %s" % rootDir)

        if self._lookFolder is None:
            userConf = path.join(rootDir, "config.json")
        else:
            userConf = path.join(self._lookFolder, "config.json")

        if path.isfile(userConf):
            logger.debug("Loading file: %s" % userConf)
            jsonData = {}
            try:
                with open(userConf, mode="r") as inFile:
                    jsonData = json.loads(inFile.read())

                self.apiUser = jsonData.get("apiUsername", "")
                self.apiPass = jsonData.get("apiPassword", "")
                self.apiURL  = jsonData.get("apiURL", "")

                self._confPath = userConf

            except Exception as e:
                logger.error("Failed to parse config JSON data.")
                logger.error(str(e))
                return False

        else:
            logger.debug("No file: %s" % userConf)

        return

# END Class Config
