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

from os import path

logger = logging.getLogger(__name__)

class Sentinel():

    def __init__(self, dataPath):

        if path.isdir(dataPath):
            self._dataPath = dataPath
        else:
            logger.error("Data folder does not exist: %s" % dataPath)
            raise FileNotFoundError("Data folder does not exist: %s" % dataPath)

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

    ##
    #  Methods
    ##

# END Class Sentinel
