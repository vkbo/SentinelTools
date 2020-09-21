# -*- coding: utf-8 -*-

from sentinel.utils import isValidUUID4, parseSizeString

def testValidUUID4():
    assert not isValidUUID4(0)
    assert not isValidUUID4("invalid")
    assert isValidUUID4("d606fa74bbb745ebae17131b60de5c1c")
    assert isValidUUID4("d606fa74-bbb7-45eb-ae17-131b60de5c1c")

def testParseSize():
    assert parseSizeString("1") == 1
    assert parseSizeString("1 B") == 1
    assert parseSizeString("1 kB") == 1024
    assert parseSizeString("1.1 kB") == 1126
    assert parseSizeString("10.1 kB") == 10342
    assert parseSizeString("1 MB") == 1048576
    assert parseSizeString("1.1 MB") == 1153434
    assert parseSizeString("10.1 MB") == 10590618
    assert parseSizeString("1 GB") == 1073741824
    assert parseSizeString("1.1 GB") == 1181116006
    assert parseSizeString("10.1 GB") == 10844792422
    assert parseSizeString("510.1 GB") == 547715704422
