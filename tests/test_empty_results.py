#!/usr/bin/env python
import unittest

import memeitizer


URL = "https://indianexpress.com/section/lifestyle/health/feed/"


class Test(unittest.TestCase):
    def test_empty_result(self):
        timestamps = memeitizer.search(URL, from_date="2080")

        assert len(timestamps) == 0

        pack = memeitizer.Pack(
            URL,
            timestamps=timestamps,
        )
        assert len(pack.timestamps) == 0
