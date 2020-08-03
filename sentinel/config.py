# -*- coding: utf-8 -*-
"""Machine Ocean Config Class

 Config class for the Machine Ocean Toolbox
"""

import sys
import json
import logging

from os import path

logger = logging.getLogger(__name__)

class Config():

    def __init__(self):

        self._packRoot = None

        # Config Settings
        self.apiUser = ""
        self.apiPass = ""
        self.apiURL  = ""

        self._loadConfig()

        return

    def __str__(self):
        """Return a string of the content of the class.
        """
        return (
            "API Username: {apiUser:s}\n"
            "API Password: {apiPass:s}\n"
            "API URL:      {apiURL:s}\n"
        ).format(
            apiUser = self.apiUser,
            apiPass = "*"*len(self.apiPass),
            apiURL  = self.apiURL,
        )

    ##
    #  Internal Functions
    ##

    def _loadConfig(self):
        """Load the config files, if they exist, and extract the data.
        """
        self._packRoot = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
        rootDir = path.abspath(path.join(self._packRoot, path.pardir))
        logger.debug("Package root directory is: %s" % rootDir)

        userConf = path.join(rootDir, "config.json")
        if path.isfile(userConf):
            logger.debug("Loading file: %s" % userConf)
            jsonData = {}
            try:
                with open(userConf, mode="r") as inFile:
                    jsonData = json.loads(inFile.read())
                if "apiUsername" in jsonData:
                    self.apiUser = jsonData["apiUsername"]
                if "apiPassword" in jsonData:
                    self.apiPass = jsonData["apiPassword"]
                if "apiURL" in jsonData:
                    self.apiURL = jsonData["apiURL"]

            except Exception as e:
                logger.error("Failed to parse config JSON data.")
                logger.error(str(e))
                return False

        else:
            logger.debug("No file: %s" % confFile)

        return

# END Class Config
