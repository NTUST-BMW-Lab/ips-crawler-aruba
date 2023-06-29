import os
from dotenv import load_dotenv
import unittest as ut
from unittest import mock

from retrieve_rssi import retrieve_rssi

load_dotenv()

class TestRetrieveRSSI(ut.TestCase, response_mock=dict()):
    @mock.patch('request.get')
    def test_retrieve_rssi(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            'response': 'mock_response'
        }
        mock_response.return_value = mock_response

        aopsid = os.getenv('ARUBA_API_TOKEN')

        

