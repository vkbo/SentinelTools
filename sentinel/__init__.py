# -*- coding: utf-8 -*-
"""Sentinel Tools

 Sentinel Tools - Main Init
============================
 Package initialisation

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

import os
import logging

__package__    = "sentinel"
__author__     = "Veronica Berglyd Olsen"
__copyright__  = "Copyright 2020, MET Norway (Machine Ocean Project)"
__license__    = "GPLv3"
__maintainer__ = "Veronica Berglyd Olsen"
__email__      = "vkbo@met.no"
__url__        = "https://github.com/vkbo/SentinelTools"
__credits__    = [
    "Veronica Berglyd Olsen",
]


from .autoapi import AutoAPI
from .config import Config
from .sentinelone import SentinelOne

__all__ = [
    "AutoAPI",
    "Config",
    "SentinelOne",
]

# Initiating logging
strLevel = os.environ.get("SENTINEL_LOGLEVEL", "INFO")
if hasattr(logging, strLevel):
    logLevel = getattr(logging, strLevel)
else:
    print("Invalid logging level '%s' in environment variable SENTINEL_LOGLEVEL" % strLevel)
    logLevel = logging.INFO

if logLevel < logging.INFO:
    logFormat = "[{asctime:s}] {levelname:8s} {message:}"
else:
    logFormat = "{levelname:8s} {message:}"

logging.basicConfig(format=logFormat, style="{", level=logLevel)
logger = logging.getLogger(__name__)
