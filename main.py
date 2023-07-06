import os
import sys
import pandas as pd
import requests
import json
from controller.session_controller import get_aruba_id
from controller.show_command import list_show_command

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from dotenv import load_dotenv


load_dotenv()

    
if __name__ == '__main__':
    
    ARUBA_USERNAME = os.getenv('ARUBA_USERNAME')
    ARUBA_PASSWORD = os.getenv('ARUBA_PASSWORD')
    ARUBA_TOKEN = os.getenv('ARUBA_API_TOKEN')
    ARUBA_IPADDRESS = os.getenv('ARUBA_IPADDRESS')
    print(ARUBA_USERNAME)
    print(ARUBA_PASSWORD)
    print(ARUBA_TOKEN)

    token = get_aruba_id(ARUBA_USERNAME,ARUBA_PASSWORD,ARUBA_IPADDRESS)
    command = 'show+ap+monitor+ap-list+ap-name+IY_1F_AP01'
    list_ap_database = list_show_command(ARUBA_IPADDRESS,token,command)
    print(list_ap_database['Monitored AP Table'])