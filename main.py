from dotenv import load_dotenv
import os
import json
import sys
import pandas as pd
import requests
import json
from controller.session_controller import get_aruba_id
from controller.show_command import list_show_command
from controller.db_controller import Database

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


load_dotenv()

if __name__ == '__main__':

    database = Database()
    database.connect()

    collection_name = 'AP'

    ARUBA_USERNAME = os.getenv('ARUBA_USERNAME')
    ARUBA_PASSWORD = os.getenv('ARUBA_PASSWORD')
    ARUBA_IPADDRESS = os.getenv('ARUBA_IPADDRESS')
    print(ARUBA_USERNAME)
    print(ARUBA_PASSWORD)
    print(ARUBA_IPADDRESS)

    while True:
        ap_names = ['IY_1F_AP01', 'IY_1F_AP03',
                    'IY_1F_AP05', 'IY_1F_AP07', 'IY_1F_AP09']
        for ap_name in ap_names:
            token = get_aruba_id(
                ARUBA_USERNAME, ARUBA_PASSWORD, ARUBA_IPADDRESS)
            command = 'show+ap+monitor+ap-list+ap-name+' + ap_name
            list_ap_database = list_show_command(
                ARUBA_IPADDRESS, token, command)
            ap_data = list_ap_database['Monitored AP Table']
            for document in ap_data:
                document['ap_name'] = ap_name
            database.insert_documents(collection_name, ap_data)
