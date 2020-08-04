# -*- coding: utf-8 -*-

from sentinel.config import Config

def testConfigInit(stInput):
    sConf = Config(lookFolder=stInput)
    assert sConf._lookFolder is not None
    assert sConf.apiUser == "user"
    assert sConf.apiPass == "password"
    assert sConf.apiURL
