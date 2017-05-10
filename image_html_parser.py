#!/usr/bin/env python
# -*- coding: utf-8 -*-
import html.parser

class Parser(html.parser.HTMLParser):

    def __init__(self):
        html.parser.HTMLParser.__init__(self)
        self.image_urls = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attribute in attrs:
                name = attribute[0]
                value = attribute[1]
                if name == "data-href":
                    self.image_urls.append(value)
                    break

    def getimageurls(self):
        return self.image_urls
