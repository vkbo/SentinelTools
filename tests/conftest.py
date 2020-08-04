# -*- coding: utf-8 -*-
"""Sentinel Tools Test Config
"""

import sys, pytest, shutil
from os import path, mkdir

sys.path.insert(1, path.abspath(path.join(path.dirname(__file__), path.pardir)))

@pytest.fixture(scope="session")
def stTemp():
    testDir = path.dirname(__file__)
    tempDir = path.join(testDir, "temp")
    if path.isdir(tempDir):
        shutil.rmtree(tempDir)
    if not path.isdir(tempDir):
        mkdir(tempDir)
    return tempDir

@pytest.fixture(scope="session")
def stInput():
    testDir = path.dirname(__file__)
    inDir = path.join(testDir, "input")
    return inDir

@pytest.fixture(scope="session")
def stRef():
    testDir = path.dirname(__file__)
    refDir = path.join(testDir, "reference")
    return refDir
