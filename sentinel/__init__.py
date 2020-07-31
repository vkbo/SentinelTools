# -*- coding: utf-8 -*-
"""Sentinel Tools

 Sentinel Tools - Main Init
============================
 Package initialisation

 This file is a part of Sentinel Tools
 Copyright 2020, Veronica Berglyd Olsen and MET Norway

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful, but
 WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import logging

__package__    = "SentinelTools"
__author__     = "Veronica Berglyd Olsen"
__copyright__  = "Copyright 2020, Veronica Berglyd Olsen and MET Norway"
__license__    = "GPLv3"
__maintainer__ = "Veronica Berglyd Olsen"
__email__      = "vkbo@met.no"
__url__        = "https://github.com/vkbo/SentinelTools"
__credits__    = [
    "Veronica Berglyd Olsen",
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
