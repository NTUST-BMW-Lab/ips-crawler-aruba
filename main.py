from dotenv import load_dotenv
import datetime
import os
import time
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
from controller.hashing import hash_data

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


load_dotenv()

if __name__ == '__main__':

    database = Database()
    database.connect()

    collection_name = 'AP'
    count = 0

    ap_names = ['IY_1F_AP01', 'D1_1F_AP01', 'D1_1F_AP02', 'D1_1F_AP03', 'D1_1F_AP04'
                'D1_1F_AP05', 'D1_1F_AP06', 'D1_1F_AP07', 'D1_1F_AP08']

    ARUBA_USERNAME = os.getenv('ARUBA_USERNAME')
    ARUBA_PASSWORD = os.getenv('ARUBA_PASSWORD')
    ARUBA_IPADDRESS = os.getenv('ARUBA_IPADDRESS')

    while True:
        data_rows = {}
        for ap_name in ap_names:
            for essid, chan in data_rows.keys():
                data_rows[(essid, chan)][f"rssi_{ap_name}"] = ''
            try:
                token = get_aruba_id(
                    ARUBA_IPADDRESS,
                    ARUBA_USERNAME,
                    ARUBA_PASSWORD)
            except Exception as e:
                print(e)
            command = 'show+ap+monitor+ap-list+ap-name+' + ap_name
            list_ap_database = list_show_command(
                ARUBA_IPADDRESS, token, command)
            print(ap_name)

            try:
                for ap in list_ap_database['Monitored AP Table']:
                    ap['bssid'] = hash_data(ap['bssid'])
            except Exception as e:
                print(e)

            try:
                # list_ap_database = list_show_command_test(ap_name)
                list_ap_database['count'] = count
                list_ap_database['timestamp'] = datetime.datetime.now()
                list_ap_database['ap_name'] = ap_name
                print(list_ap_database)

                database.insert_raw_documents('raw_crawl', list_ap_database)

                ap_data = list_ap_database['Monitored AP Table']

                for monitored_ap in ap_data:
                    monitored_ap['ap_name'] = ap_name
                    monitored_ap['timestamp'] = time.time()
                    monitored_ap['count'] = count
                    essid = monitored_ap['essid']

                    if 'band/chan/ch-width/ht-type' in monitored_ap:
                        band, chan, ch_width, ht_type = parse_data(
                            monitored_ap['band/chan/ch-width/ht-type'])
                    else:
                        chan = monitored_ap['chan']
                        band = ''

                    rssi_key = f"rssi_{ap_name}"

                    if (essid, chan) not in data_rows:
                        data_rows[(essid, chan)] = {
                            'count': count, 'bssid': monitored_ap['bssid'], 'chan': chan, 'band': band}

                    data_rows[(essid, chan)
                              ][rssi_key] = monitored_ap['curr-rssi']
                    print(data_rows)
                    database.insert_documents(collection_name, data_rows)
                    count += 1
            except Exception as e:
                print(e)
        time.sleep(5)
