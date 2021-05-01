#!/usr/bin/env python3
# nlantau, 2021-05-01

# Receive serial data and plot

import serial
import re
import json
import matplotlib.pyplot as plt
#from rich.progress import track

JSONFILE = "DSO138_data.json"

def main():
    data_collected = collect_data(create_dict())
    json_data = json.dumps(data_collected)
    store_data(json_data)
    plot(data_collected)


def display_info(data: dict):
    for k,v in data["info"].items():
        print(f'{k}: {v}')


def plot(data: dict):
    numeric = re.compile(r"[0-9]+")
    # VSen = float(re.search(numeric, data["info"]["VSen"]).group(0))
    numb = [int(x) for x in data["values"]]
    voltage = [float(v[1]) for _,v in data["values"].items()]
    # voltage = [float(v[1]) * VSen/2 for _,v in data["values"].items()]

    display_info(data)
    print(f'> Plotting data...')

    plt.grid()
    plt.plot(numb, voltage)
    plt.show()


def create_dict() -> dict:
    data = {}
    data['info'] = {}
    data['values'] = {}
    return data


def collect_data(data: dict) -> dict:
    alpha = re.compile(r"[A-Za-z]+")
    numeric = re.compile(r"[0-9]+")
    last_line = re.compile(r"^01023")
    first = True

    with serial.Serial(r'/dev/ttyUSB0', 115200, timeout=3) as ser:
        print(f'> Start transmission now!')
        while True:
            all_data = ser.readline().decode('utf-8').strip()
            if first:
                print(f'> Receiving data...')
                first = False
            all_data = all_data.strip(" ")
            if re.search(alpha, all_data):
                f1, f2 = all_data.split(',')
                f2 = f2.strip(" ")
                data['info'][f1] = f2
            elif re.search(numeric, all_data):
                f1, f2, f3 = all_data.split(',')
                f3 = f3.strip(" ")
                data['values'][f1] = [f2,f3]
            if re.search(last_line, all_data):
                print(f'> All data received.\n> Closing serial connection.')
                break
    return data


def store_data(json_data: json) -> None:
    with open(JSONFILE, "w") as f:
        f.write(json_data)
        print(f'> Saved to {JSONFILE}.')


if __name__ == "__main__":
    main()