import os
import sys
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

ARUBA_USERNAME = os.getenv('ARUBA_USERNAME')
ARUBA_PASSWORD = os.getenv('ARUBA_PASSWORD')
ARUBA_TOKEN = os.getenv('ARUBA_API_TOKEN')

if __name__ == '__main__':
    pass