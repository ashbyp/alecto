import unittest
from utils import config


class ConfigTest(unittest.TestCase):

    def test_get_config(self):
        conf = config.get()
        self.assertTrue('public' in conf)
        self.assertTrue('private' in conf)
        self.assertEqual(conf['public']['gate_api.io']['api_host'], 'https://api.gateio.ws/api/v4')


