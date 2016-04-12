import unittest

import mykids.mykids_server as server


class MykidsServerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def test_albums(self):
        rv = self.app.get('/get/albums')
        print rv.data
        assert 'No entries here so far' in rv.data
