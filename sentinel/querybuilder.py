# -*- coding: utf-8 -*-
"""Sentinel Tools Query Builder

 Sentinel Tools - Query Builder
================================
 Helper class to build search queries

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

from sentinelsat import SentinelAPI

from .constants import SQuery
from .error import SentinelFilterError

logger = logging.getLogger(__name__)

class QueryBuilder():

    def __init__(self):

        self._platformName = None

        self._queryDict = {}

        return

# END Class QueryBuilder

class FilterS1():

    def __init__(self):

        self._missionID       = None
        self._modeBeam        = None
        self._productType     = None
        self._resolutionClass = None
        self._processingLevel = None
        self._productClass    = None

        return

    def setMissionID(self, missionID):
        """Set the Sentinel-1 mission ID, value MMM.
        """
        if missionID in ("A", "S1A"):
            self._missionID = "S1A"
        elif missionID in ("B", "S1B"):
            self._missionID = "S1B"
        else:
            self._missionID = None
            raise SentinelFilterError(
                "Invalid Filter\n"
                "Sentinel-1 Mission ID must be one of the following:\n"
                " * 'S1A' or 'A' for the Sentinel-1A mission\n"
                " * 'S1B' or 'B' for the Sentinel-1B mission\n"
            )
        return

    def setModeOrBeam(self, modeBeam):
        """Set the Sentinel-1 Mode/Beam, value BB.
        """
        if modeBeam == "SM":
            self._modeBeam = "S*"
        elif modeBeam in ("S1", "S2", "S3", "S4", "S5", "S6", "IW", "EW", "WV"):
            self._modeBeam = modeBeam
        else:
            self._modeBeam = None
            raise SentinelFilterError(
                "Invalid Filter\n"
            )
        return

# END Class FilterS1
