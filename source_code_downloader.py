#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request

class Downloader():
    def download_source(self, url = "", debug = False):
        if url == "":
            raise ValueError("Urls can not be empty!")

        response = urllib.request.urlopen(url)
        responseData = response.read().decode()
        self.print_debug(response, responseData, debug)
        return responseData

    def print_debug(self, httpResponse, httpData, debug):
        if debug:
            responseCode = str(httpResponse.getcode())
            responseUrl = httpResponse.geturl()
            responseObject = str(httpResponse)
            responseData = httpData

            print("Code: " + responseCode)
            print("Url: " + responseUrl)
            print("HTTPResponse-Object: " + responseObject)
            print("ResponseRead(): " + responseData)
