from dotenv import load_dotenv
import time
import os
import json
import sys
import pandas as pd
import requests
import json
from controller.session_controller import get_aruba_id
from controller.show_command import list_show_command
from controller.db_controller import Database
from controller.show_command_test import list_show_command_test
from controller.parse_data import parse_data

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


load_dotenv()

if __name__ == '__main__':

    database = Database()
    database.connect()

    collection_name = 'AP'
    count = 0

    ap_names = ['IY_1F_AP01', 'IY_1F_AP03',
                'IY_1F_AP05', 'IY_1F_AP07', 'IY_1F_AP09']

    ARUBA_USERNAME = os.getenv('ARUBA_USERNAME')
    ARUBA_PASSWORD = os.getenv('ARUBA_PASSWORD')
    ARUBA_IPADDRESS = os.getenv('ARUBA_IPADDRESS')
    print(ARUBA_USERNAME)
    print(ARUBA_PASSWORD)
    print(ARUBA_IPADDRESS)

    while True:
        data_rows = {}
        for ap_name in ap_names:
            essids = data_rows.keys()
            for essid in essids:
                data_rows[essid][f"rssi_{ap_name}"] = ''
            token = get_aruba_id(
                ARUBA_IPADDRESS,
                ARUBA_USERNAME,
                ARUBA_PASSWORD)
            command = 'show+ap+monitor+ap-list+ap-name+' + ap_name
            list_ap_database = list_show_command(
                ARUBA_IPADDRESS, token, command)
            # list_ap_database = list_show_command_test(ap_name)
            ap_data = list_ap_database['Monitored AP Table']

            for monitored_ap in ap_data:
                monitored_ap['ap_name'] = ap_name
                monitored_ap['timestamp'] = time.time()
                monitored_ap['count'] = count
                band, chan, ch_width, ht_type = parse_data(
                    monitored_ap['band/chan/ch-width/ht-type'])

                essid = monitored_ap['essid']
                rssi_key = f"rssi_{ap_name}"

                if essid not in data_rows:
                    data_rows[essid] = {
                        'count': count, 'bssid': monitored_ap['bssid'], 'band': band, 'chan': chan, 'ch_width': ch_width, 'ht_type': ht_type}

                data_rows[essid][rssi_key] = monitored_ap['curr-rssi']

        print(data_rows)
        database.insert_documents(collection_name, data_rows)
        count += 1
        time.sleep(15)
