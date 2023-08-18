from dotenv import load_dotenv
import datetime
import time
import pandas as pd
import requests
from controller.session_controller import get_aruba_id
from controller.show_command import list_show_command
from controller.db_controller import Database
from func_test.show_command_test import list_show_command_test
from controller.parse_data import parse_data
from controller.hashing import create_hash
from controller.db_controller import DatabaseInterface
from controller.eirp import eirp_test

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

load_dotenv()



class APDataCollector:
    def __init__(self, ap_names: List[str], rssi_keys: List[str], aruba_username: str, aruba_password: str,
                 aruba_ipaddress: str, database: DatabaseInterface):
        self.ap_names = ap_names
        self.rssi_keys = rssi_keys
        self.ARUBA_USERNAME = aruba_username
        self.ARUBA_PASSWORD = aruba_password
        self.ARUBA_IPADDRESS = aruba_ipaddress
        self.database = database

    def get_aruba_token(self):
        try:
            token = get_aruba_id(
                self.ARUBA_IPADDRESS,
                self.ARUBA_USERNAME,
                self.ARUBA_PASSWORD
            )
            return token
        except Exception as e:
            print(e)
            return None

    def get_ap_data(self, token, ap_name):
        try:
            command = 'show+ap+monitor+ap-list+ap-name+' + ap_name
            list_ap_database = list_show_command(self.ARUBA_IPADDRESS, token, command)
            return list_ap_database
        except Exception as e:
            print(e)
            return None

    def get_eirp_data(self, token, ap_name):
        try:
            command = 'show+ap+active+details'
            eirptest = list_show_command(self.ARUBA_IPADDRESS, token, command)
            for ap in eirptest['Active AP Table']:
                if ap['Name'] == ap_name:
                    return ap['Radio 0 Band Ch/EIRP/MaxEIRP/Clients'], ap['Radio 1 Band Ch/EIRP/MaxEIRP/Clients']
            return '', ''
        except Exception as e:
            print(e)
            return '', ''

    def collect_and_store_data(self):
        self.database.connect()
        collection_name = 'AP'
        count = 0
        while True:
            data_rows = {}
            token = self.get_aruba_token()
            if token is None:
                time.sleep(5)
                continue
            for ap_name in self.ap_names:
                list_ap_database = self.get_ap_data(token, ap_name)
                if list_ap_database is None:
                    list_ap_database = list_show_command(ap_name)

                for ap in list_ap_database['Monitored AP Table']:
                    ap['bssid'] = create_hash(ap['bssid'])

                radio0_eirp, radio1_eirp = self.get_eirp_data(token, ap_name)
                list_ap_database['Radio0_EIRP'] = radio0_eirp
                list_ap_database['Radio1_EIRP'] = radio1_eirp

                try:
                    list_ap_database['count'] = count
                    list_ap_database['timestamp'] = datetime.datetime.now()
                    list_ap_database['ap_name'] = ap_name

                    self.database.insert_raw_documents('raw_crawl', list_ap_database)

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

                        data_rows[(essid, chan)][rssi_key] = monitored_ap['curr-rssi']
                        self.database.insert_documents(collection_name, data_rows)

                except Exception as e:
                    print(e)
            time.sleep(5)
            count += 1
