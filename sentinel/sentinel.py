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

from sentinelsat import SentinelAPI

from .config import Config
from .autoapi import AutoAPI

logger = logging.getLogger(__name__)

class Sentinel():

    def __init__(self, api=None):

        self._theAPI = None

        if isinstance(api, SentinelAPI):
            self._theAPI = api
        elif isinstance(api, AutoAPI):
            self._theAPI = api.getAPI()
        else:
            raise ValueError("Attribute 'api' must be a SentinelAPI or AutoAPI object")

        return

# END Class Sentinel
