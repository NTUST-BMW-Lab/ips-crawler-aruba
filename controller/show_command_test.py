import json


def list_show_command_test(ap_names):
    if ap_names == 'IY_1F_AP01':
        return {
            "Monitored AP Table": [
                {
                    "ap-type": "valid",
                    "band/chan/ch-width/ht-type": "5GHz/140E/80MHz/VHT",
                    "bssid": "44:52:1E:CC:F0:28",
                    "curr-rssi": "65",
                    "essid": "eduroam"
                },
                {
                    "ap-type": "invalid",
                    "band/chan/ch-width/ht-type": "5GHz/140E/80MHz/VHT",
                    "bssid": "FF:4E:5B:01:70:43",
                    "curr-rssi": "73",
                    "essid": "office_wifi"
                },
                {
                    "ap-type": "valid",
                    "band/chan/ch-width/ht-type": "5GHz/140E/80MHz/VHT",
                    "bssid": "1C:5A:04:3D:62:DA",
                    "curr-rssi": "60",
                    "essid": "wifi_network"
                }
            ]
        }
    elif ap_names == 'IY_1F_AP03':
        return {
            "Monitored AP Table": [
                {
                    "ap-type": "invalid",
                    "band/chan/ch-width/ht-type": "5GHz/140E/80MHz/VHT",
                    "bssid": "BC:8B:5B:A0:C6:93",
                    "curr-rssi": "64",
                    "essid": "home_wifi"
                },
                {
                    "ap-type": "invalid",
                    "band/chan/ch-width/ht-type": "5GHz/140E/80MHz/VHT",
                    "bssid": "63:C2:E1:54:74:55",
                    "curr-rssi": "57",
                    "essid": "wifi_network"
                },
                {
                    "ap-type": "valid",
                    "band/chan/ch-width/ht-type": "5GHz/140E/80MHz/VHT",
                    "bssid": "AD:FA:5A:8C:3D:28",
                    "curr-rssi": "40",
                    "essid": "office_wifi"
                }
            ]
        }
    elif ap_names == 'IY_1F_AP05':
        return {
            "Monitored AP Table": [
                {
                    "ap-type": "valid",
                    "band/chan/ch-width/ht-type": "5GHz/140E/80MHz/VHT",
                    "bssid": "3A:C4:D3:1D:4B:F1",
                    "curr-rssi": "80",
                    "essid": "wifi_network"
                },
                {
                    "ap-type": "invalid",
                    "band/chan/ch-width/ht-type": "2.4GHz/6/20MHz/HT",
                    "bssid": "85:A7:19:C3:72:62",
                    "curr-rssi": "71",
                    "essid": "home_wifi"
                },
                {
                    "ap-type": "invalid",
                    "band/chan/ch-width/ht-type": "2.4GHz/6/20MHz/HT",
                    "bssid": "F0:16:E1:75:7C:2F",
                    "curr-rssi": "67",
                    "essid": "office_wifi"
                }
            ]
        }
    elif ap_names == 'IY_1F_AP07':
        return {
            "Monitored AP Table": [
                {
                    "ap-type": "invalid",
                    "band/chan/ch-width/ht-type": "5GHz/140E/80MHz/VHT",
                    "bssid": "2F:AD:76:D0:5C:1F",
                    "curr-rssi": "76",
                    "essid": "home_wifi"
                },
                {
                    "ap-type": "valid",
                    "band/chan/ch-width/ht-type": "2.4GHz/6/20MHz/HT",
                    "bssid": "10:CC:51:85:F9:20",
                    "curr-rssi": "68",
                    "essid": "eduroam"
                },
                {
                    "ap-type": "invalid",
                    "band/chan/ch-width/ht-type": "5GHz/140E/80MHz/VHT",
                    "bssid": "7B:B1:75:AE:99:22",
                    "curr-rssi": "70",
                    "essid": "office_wifi"
                }
            ]
        }
    elif ap_names == 'IY_1F_AP09':
        return {
            "Monitored AP Table": [
                {
                    "ap-type": "invalid",
                    "band/chan/ch-width/ht-type": "5GHz/140E/80MHz/VHT",
                    "bssid": "E1:21:11:FC:45:14",
                    "curr-rssi": "79",
                    "essid": "eduroam"
                },
                {
                    "ap-type": "invalid",
                    "band/chan/ch-width/ht-type": "2.4GHz/6/20MHz/HT",
                    "bssid": "0A:B5:E5:D5:98:40",
                    "curr-rssi": "78",
                    "essid": "office_wifi"
                },
                {
                    "ap-type": "valid",
                    "band/chan/ch-width/ht-type": "5GHz/140E/80MHz/VHT",
                    "bssid": "4D:D7:E5:80:D0:AD",
                    "curr-rssi": "49",
                    "essid": "wifi_network"
                }
            ]
        }
