# -*- coding: utf-8 -*-
"""Sentinel Tools API Class

 Sentinel Tools - API Class
============================
 Wrapper class for the Sentinel (Copernicus) API

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

from .config import Config

logger = logging.getLogger(__name__)

class SentinelAPI():

    def __init__(self, username="", password="", url=""):

        self._apiUser = ""
        self._apiPass = ""
        self._apiURL  = ""

        self.apiUser = username
        self.apiPass = password
        self.apiURL  = url

        return

    @classmethod
    def fromConfig(cls, config):
        """Instansiate from a sentinel.Config object.
        """
        if isinstance(config, Config):
            return cls(config.apiUser, config.apiPass, config.apiURL)
        else:
            raise ValueError("Property 'config' is not an instance of sentinel.Config")
        return cls()

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
            raise ValueError("Property 'username' must be a string")
        return

    @apiPass.setter
    def apiPass(self, password):
        if isinstance(password, str):
            self._apiPass = password
        else:
            raise ValueError("Property 'password' must be a string")
        return

    @apiURL.setter
    def apiURL(self, url):
        if isinstance(url, str):
            self._apiURL = url
        else:
            raise ValueError("Property 'url' must be a string")
        return

# END Class SentinelAPI
