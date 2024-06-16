#!/usr/bin/env python
import unittest

import memeitizer

URL = "https://berniesanders.com/"
TIMESTAMP = "20160106120201"
REDIRECT_LANGUAGE = b"Got an HTTP 301 response at crawl time"


class Test(unittest.TestCase):
    def test_no_redirect(self):
        asset = memeitizer.Asset(URL, TIMESTAMP)
        content = asset.fetch()
        assert len(content) == 0

    def test_yes_redirect(self):
        session = memeitizer.Session(follow_redirects=True)
        asset = memeitizer.Asset(URL, TIMESTAMP)
        content = asset.fetch(session=session)
        assert REDIRECT_LANGUAGE not in content
        assert b"Nobody who works 40 hours" in content
