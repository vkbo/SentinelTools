# -*- coding: utf-8 -*-

import pytest

from sentinelsat import SentinelAPI

from sentinel import Config, AutoAPI

def testConfigInit(stInput):
    sConf = Config(lookFolder=stInput)
    assert sConf._lookFolder is not None
    assert sConf.apiUser == "user"
    assert sConf.apiPass == "password"
    assert sConf.apiURL  == "https://scihub.copernicus.eu/apihub"

def testAutoAPI(stInput):
    sConf = Config(lookFolder=stInput)
    sAPI = AutoAPI(sConf)
    assert isinstance(sAPI.getAPI(), SentinelAPI)
    with pytest.raises(ValueError):
        sAPI.apiUser = 1
    with pytest.raises(ValueError):
        sAPI.apiPass = 1
    with pytest.raises(ValueError):
        sAPI.apiURL = 1
