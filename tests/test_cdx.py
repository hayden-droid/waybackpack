#!/usr/bin/env python
import unittest

import memeitizer


class Test(unittest.TestCase):
    def test_snapshot_index(self):
        url = "http://www.dol.gov/"
        snapshots = memeitizer.search(url)
        assert len(snapshots) > 0
        assert snapshots[0]["timestamp"] == "19961102145216"
        clipped = memeitizer.search(url, to_date="1996")
        assert len(clipped) < len(snapshots)
        assert len(clipped) == 5

    def test_uniques(self):
        url = "http://www.dol.gov/"
        uniques = memeitizer.search(url, to_date="1996", uniques_only=True)
        assert len(uniques) == 2
