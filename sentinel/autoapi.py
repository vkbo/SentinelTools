# -*- coding: utf-8 -*-
"""Sentinel Tools API Class

 Sentinel Tools - API Class
============================
 Simple wrapper class for the Sentinel API that takes a Config object.

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

from sentinelsat import SentinelAPI

from .config import Config

logger = logging.getLogger(__name__)

class AutoAPI():

    def __init__(self, config):

        self._theConfig = config
        self._apiUser = ""
        self._apiPass = ""
        self._apiURL  = "https://scihub.copernicus.eu"
        self._theAPI  = None

        if isinstance(config, Config):
            self.apiUser = config.apiUser
            self.apiPass = config.apiPass
            self.apiURL  = config.apiURL
        else:
            raise ValueError("Property 'config' is not an instance of sentinel.Config")

        try:
            self._theAPI = SentinelAPI(self._apiUser, self._apiPass, api_url=self._apiURL)
        except Exception as e:
            logger.error("Could not set up Sentinel API")
            logger.error(str(e))
            return

        return

    ##
    #  Properties
    ##

    @property
    def apiUser(self):
        return self._apiUser

    @property
    def apiPass(self):
        return self._apiPass

    @property
    def apiURL(self):
        return self._apiURL

    ##
    #  Setters
    ##

    @apiUser.setter
    def apiUser(self, username):
        if isinstance(username, str):
            self._apiUser = username
        else:
            raise ValueError("Attribute 'username' must be a string")
        return

    @apiPass.setter
    def apiPass(self, password):
        if isinstance(password, str):
            self._apiPass = password
        else:
            raise ValueError("Attribute 'password' must be a string")
        return

    @apiURL.setter
    def apiURL(self, url):
        if isinstance(url, str):
            self._apiURL = url
        else:
            raise ValueError("Attribute 'url' must be a string")
        return

    ##
    #  Getters
    ##

    def getAPI(self):
        """Returns the API object.
        """
        if self._theAPI is None or not isinstance(self._theAPI, SentinelAPI):
            raise ConnectionError("Not connected to the API")
        return self._theAPI

    def getConfig(self):
        """Return the config object.
        """
        return self._theConfig

# END Class AutoAPI
