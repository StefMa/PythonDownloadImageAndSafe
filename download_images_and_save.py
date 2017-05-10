#!/usr/bin/env python
# -*- coding: utf-8 -*-
import source_code_downloader
import image_html_parser
import urllib.request
import os

# Prepare folders and urls
base_folder = "output/"
folders = [base_folder + "devlogos", base_folder + "random"]
base_url = "https://gist.githubusercontent.com/StefMa/7b0ec5d2c5eddb34222ba9fb6392aea0/raw/a55df028bbafaac6e33618d70417bc53eed98807/"
urls = [base_url + "devlogos.html", base_url + "random.html"]

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

for i in range(0, len(urls)):
    # Download source code
    downloader = source_code_downloader.Downloader()
    httpResponse = downloader.download_source(urls[i])

    # Get image urls
    htmlParser = image_html_parser.Parser()
    htmlParser.feed(httpResponse)
    image_urls = htmlParser.getimageurls()
    htmlParser.close()

    # Download images and save in given folder
    for j in range(0, len(image_urls)):
        urllib.request.urlretrieve(image_urls[j], str(folders[i] + "/" + "image_" + str(j) + ".jpg"))
