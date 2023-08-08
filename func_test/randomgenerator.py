import random
import json


def generate_random_data():
    data = {
        "Monitored AP Table": []
    }

    ap_types = ["valid", "invalid"]
    band_chan_ch_width_ht_types = ["5GHz/140E/80MHz/VHT", "2.4GHz/6/20MHz/HT"]
    essids = ["eduroam", "wifi_network", "home_wifi", "office_wifi"]

    for _ in range(3):
        entry = {
            "ap-type": random.choice(ap_types),
            "band/chan/ch-width/ht -type": random.choice(band_chan_ch_width_ht_types),
            "bssid": generate_random_bssid(),
            "curr-rssi": str(random.randint(40, 80)),
            "essid": random.choice(essids)
        }
        data["Monitored AP Table"].append(entry)

    return data


def generate_random_bssid():
    hex_chars = "0123456789ABCDEF"
    bssid = ""
    for _ in range(6):
        bssid += random.choice(hex_chars)
        bssid += random.choice(hex_chars)
        bssid += ":"
    bssid = bssid[:-1]  # Remove the last colon

    return bssid


# Generate random data and print it
for i in range(5):
    random_data = generate_random_data()
    file_name = f"random_data_{i+1}.json"
    with open(file_name, "w") as f:
        json.dump(random_data, f, indent=4)
    print(f"Saved random data to {file_name}")
