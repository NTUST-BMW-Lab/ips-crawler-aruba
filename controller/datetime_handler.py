import datetime as dt

def convert_datetime(df):
    hours = 8
    current_time = dt.datetime.now()
    ts = current_time - dt.timedelta(hours=hours)
    ts_tw_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    data_json = df.to_json(orient='records')

    for data in data_json:
        data['ts'] = ts
        data['DatetiimeStr'] = ts_tw_str
        data['DateTime'] = current_time