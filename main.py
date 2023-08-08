from dotenv import load_dotenv
import os
from controller.APDataCollector import APDataCollector
from controller.db_controller import Database


load_dotenv()

if __name__ == '__main__':
    ap_names = ['D1_1F_AP01', 'D1_1F_AP02', ...]  # Your AP names
    rssi_keys = ['rssi_D1_1F_AP01', 'rssi_D1_1F_AP02', ...]  # Your RSSI keys
    aruba_username = os.getenv('ARUBA_USERNAME')
    aruba_password = os.getenv('ARUBA_PASSWORD')
    aruba_ipaddress = os.getenv('ARUBA_IPADDRESS')

    database = Database()
    data_controller = APDataCollector(
        ap_names, rssi_keys, aruba_username, aruba_password, aruba_ipaddress, database)
    data_controller.collect_and_store_data()
