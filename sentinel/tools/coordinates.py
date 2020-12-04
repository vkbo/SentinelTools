# -*- coding: utf-8 -*-
"""Sentinel Utilities

 Sentinel Tools - Coordinates
==============================
 For working with coordinates

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
import math
import json

logger = logging.getLogger(__name__)

E_POL_CIRC = 40007863.0 # Polar circumference (m)
E_EQ_CIRC  = 40075017.0 # Equatorial circumferece (m)

C_RAD = math.pi/180.0 # Degree to radians

def pointPolygon(radius, longitude, latitude, points=6, prec=8):
    """Calculate a polygon around a given coordinate, with a given
    radius. This uses a simple spherical model of the earth.
    """
    if radius <= 0.0:
        # Nothing to do
        return [(longitude, latitude)]

    if points < 3:
        raise ValueError("Number of polygon points cannot be less than 3")

    latDeg = E_POL_CIRC/360.0
    lngDeg = E_EQ_CIRC/360.0

    retCoords = []
    dA = 2.0*math.pi/points
    for a in range(0, points):
        rX = radius*math.cos(a*dA)
        rY = radius*math.sin(a*dA)
        latA = round(latitude + rY/latDeg, prec)
        lngA = round(longitude + rX/(lngDeg*math.cos(C_RAD*latA)), prec)
        retCoords.append((lngA, latA))

    retCoords.append(retCoords[0])

    return retCoords

def pointsToGeoJson(points):

    polyMap = []
    for lng, lat in points:
        polyMap.append([lng, lat])

    geoDict = {
        "geometry": {
            "type": "Polygon",
            "coordinates": [polyMap],
        }
    }

    return json.dumps(geoDict, indent=2)
