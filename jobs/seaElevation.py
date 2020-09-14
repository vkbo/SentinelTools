# -*- coding: utf-8 -*-

import sys
import json

from os import environ, path

# Set up local package environment and logging
thisDir = path.abspath(path.dirname(__file__))
rootDir = path.abspath(path.join(thisDir, path.pardir))
sys.path.insert(1, rootDir)
environ["SENTINEL_LOGLEVEL"] = "DEBUG"

# Tools import
from sentinel import logger, Config, AutoAPI # noqa: E402
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt # noqa: E402

logger.debug("Script dir: %s" % rootDir)

# API configuration
sConf = Config(apiName="eumetsat")
sConf.printInfo()

sAPI = AutoAPI(sConf)
cAPI = sAPI.getAPI()

fpFile = path.join(rootDir, "tests", "input", "map.geojson")
fpMap = geojson_to_wkt(read_geojson(fpFile))

cQuery = SentinelAPI.format_query(
    area = fpMap,
    raw  = (
        "("
        "platformname:Sentinel-3 "
        "AND producttype:SR_2_WAT___ "
        "AND instrumentshortname:SRAL "
        "AND productlevel:L2"
        ")"
    ),
    date = ("2020-05-01T00:00:00Z", "2020-05-31T23:59:59Z")
)
# print(cQuery)

nResult = cAPI.count(raw=cQuery)
logger.info("Query matched %d datasets" % nResult)

# qDict = cAPI.query(raw=cQuery)
# print(json.dumps(qDict, indent=2))
