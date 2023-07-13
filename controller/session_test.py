import os
import unittest as ut
from unittest import mock
import requests
from dotenv import load_dotenv

from show_command import list_show_command

load_dotenv()


class TestListShowCommand(ut.TestCase):
    @mock.patch('request.get')
    def test_list_show_command_success(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'response': 'mock_data'}
        mock_response.return_value = mock_response

        # Test Input Values
        aopsid = os.getenv('ARUBA_API_TOKEN')
        aruba_id = ''
        command = ''

        # Call function to test
        response = list_show_command(aopsid, aruba_id, command)

        self.assertEqual(response, {'response': 'mock_data'})

        mock_get.assert_called_once_with(
            f"https://{aopsid}:4343/v1/configuration/showcommand?command={command}&UIDARUBA={aruba_id}",
            cookies={'SESSION': aruba_id},
            verify=False
        )

    @mock.patch('request.get')
    def test_list_show_command_failure(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Test Input Values
        aopsid = os.getenv('ARUBA_API_TOKEN')
        aruba_id = ''
        command = ''

        # Call the function to test
        response = list_show_command(aopsid, aruba_id, command)

        self.assertEqual(response, '')

        mock_get.assert_called_once_with(
            f"https://{aopsid}:4343/v1/configuration/showcommand?command={command}&UIDARUBA={aruba_id}",
            cookies={'SESSION': aruba_id},
            verify=False
        )
