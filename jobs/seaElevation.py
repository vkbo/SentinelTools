# -*- coding: utf-8 -*-

import sys

from os import environ, path

# Set up local package environment and logging
thisDir = path.abspath(path.dirname(__file__))
rootDir = path.abspath(path.join(thisDir, path.pardir))
sys.path.insert(1, rootDir)
environ["SENTINEL_LOGLEVEL"] = "DEBUG"

# Tools import
from sentinel import logger, Config, AutoAPI, Sentinel # noqa: E402
from sentinelsat import SentinelAPI # noqa: E402

logger.debug("Script dir: %s" % rootDir)

# API configuration
sConf = Config(apiName="eumetsat")
sConf.printInfo()

sAPI = AutoAPI(sConf)
sData = Sentinel(sConf.dataPath)
cAPI = sAPI.getAPI()
fpMap = (
    "POLYGON(("
    "-19.4134 50.4665, "
    " 38.8403 50.4665, "
    " 38.8403 79.3619, "
    "-19.4134 79.3619, "
    "-19.4134 50.4665"
    "))"
)
fpQuery = (
    "("
    "platformname:Sentinel-3 "
    "AND producttype:SR_2_WAT___ "
    "AND instrumentshortname:SRAL "
    "AND productlevel:L2"
    ")"
)

cQuery = SentinelAPI.format_query(
    area = fpMap,
    raw  = fpQuery,
    date = ("2019-08-01T00:00:00Z", "2019-09-13T23:59:59Z")
)
# print(cQuery)

nResult = cAPI.count(raw=cQuery)
logger.info("Query matched %d datasets" % nResult)

qDict = cAPI.query(raw=cQuery)
for aKey, aDataSet in qDict.items():
    print(aKey)
    for dKey, dValue in aDataSet.items():
        print("%s:" % dKey, dValue)
    break
