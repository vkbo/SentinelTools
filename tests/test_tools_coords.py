# -*- coding: utf-8 -*-

import pytest

from sentinel.tools import pointPolygon, pointsToGeoJson

def testTools_PointPolygon():

    # Minimal result
    assert pointPolygon(0, 50.0, 50.0) == [(50.0, 50.0)]

    # Invalid input
    with pytest.raises(ValueError):
        assert pointPolygon(50, 50.0, 50.0, points=2)

    assert pointPolygon(50e3, 0.0, 0.0, points=6, prec=2) == [
        (0.45, 0.0), (0.22, 0.39), (-0.22, 0.39), (-0.45, 0.0),
        (-0.22, -0.39), (0.22, -0.39), (0.45, 0.0)
    ]

    assert pointPolygon(50e3, -10.0, 50.0, points=6, prec=2) == [
        (-9.3, 50.0), (-9.65, 50.39), (-10.35, 50.39), (-10.7, 50.0),
        (-10.35, 49.61), (-9.65, 49.61), (-9.3, 50.0)
    ]

# END Test textTools_PointPolygon

def testTools_PointsToGeoJson():

    assert pointsToGeoJson([
        (-9.3, 50.0), (-9.65, 50.39), (-10.35, 50.39), (-10.7, 50.0),
        (-10.35, 49.61), (-9.65, 49.61), (-9.3, 50.0)
    ]) == (
        "{\n"
        "  \"geometry\": {\n"
        "    \"type\": \"Polygon\",\n"
        "    \"coordinates\": [\n"
        "      [\n"
        "        [\n"
        "          -9.3,\n"
        "          50.0\n"
        "        ],\n"
        "        [\n"
        "          -9.65,\n"
        "          50.39\n"
        "        ],\n"
        "        [\n"
        "          -10.35,\n"
        "          50.39\n"
        "        ],\n"
        "        [\n"
        "          -10.7,\n"
        "          50.0\n"
        "        ],\n"
        "        [\n"
        "          -10.35,\n"
        "          49.61\n"
        "        ],\n"
        "        [\n"
        "          -9.65,\n"
        "          49.61\n"
        "        ],\n"
        "        [\n"
        "          -9.3,\n"
        "          50.0\n"
        "        ]\n"
        "      ]\n"
        "    ]\n"
        "  }\n"
        "}"
    )

# END Test testTools_PointsToGeoJson
