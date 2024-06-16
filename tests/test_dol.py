#!/usr/bin/env python
import unittest

import memeitizer


class Test(unittest.TestCase):
    def test_basic(self):
        url = "http://www.dol.gov/"
        snapshots = memeitizer.search(url)
        timestamps = [snap["timestamp"] for snap in snapshots]
        first = memeitizer.Asset(url, timestamps[0])
        session = memeitizer.Session(follow_redirects=True)
        content = first.fetch(session=session)
        assert b"Regulatory Information" in content
        assert len(content) > 0
