# -*- coding: utf-8 -*-
"""Sentinel Utilities

 Sentinel Tools - Utilities
============================
 Various useful functions

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

from os import path, mkdir
from uuid import UUID

logger = logging.getLogger(__name__)

def ensureFolderExists(theFolder):
    """Check if a folder exists, and if not, create it.
    """
    if not path.isdir(theFolder):
        mkdir(theFolder)
        logger.info("Created folder: %s" % theFolder)
    return path.isdir(theFolder)

def isValidUUID4(theUUID):
    """Check if a string is a valid UUID4.
    """
    if not isinstance(theUUID, str):
        return False
    try:
        _ = UUID(theUUID, version=4)
    except ValueError:
        return False
    return True

def parseSizeString(theSize):
    """Parses a size string into an integer byte value.
    """
    if not isinstance(theSize, str):
        return -1
    theBits = theSize.split()
    if len(theBits) == 1:
        try:
            return int(round(float(theBits[0])))
        except Exception:
            return -1
    elif len(theBits) > 1:
        if theBits[1].lower() == "kb":
            dScale = 1024
        elif theBits[1].lower() == "mb":
            dScale = 1024*1024
        elif theBits[1].lower() == "gb":
            dScale = 1024*1024*1024
        else:
            dScale = 1
        try:
            return int(round(float(theBits[0])*dScale))
        except Exception:
            return -1
    return -1
