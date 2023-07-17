def parse_data(data):
    components = data.split('/')
    band = components[0]
    chan = components[1]
    ch_width = components[2]
    ht_type = components[3]

    return band, chan, ch_width, ht_type
