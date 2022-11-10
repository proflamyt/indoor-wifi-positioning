import subprocess
from math import log10
import sys


def main():
    get_aps()


def calculate_abs():
    ...


def get_os():
    return sys.platform

# subprocess.Popen(['netsh', 'wlan', 'show', 'networks', 'mode=bssid']) ['netsh', 'wlan', 'show', 'interfaces'],

def get_aps(platform, interface='wlan'):
    if platform == 'win32':
        scan_cmd = subprocess.Popen(['netsh', interface, 'show', 'networks', 'mode=bssid'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        scan_out, scan_err = scan_cmd.communicate()
        scan_out_data = {}
        scan_out_lines = str(scan_out).split("\\n")[1:-1]
        for each_line in scan_out_lines:
            split_line = [e for e in each_line.split(" ") if e != ""]
            print(split_line)
            
        #     line_data = {"SSID": split_line[0], "RSSI": int(split_line[2]), "channel": split_line[3], "HT": (split_line[4] == "Y"), "CC": split_line[5], "security": split_line[6]}
        #     scan_out_data[split_line[1]] = line_data
        # return scan_out_data
    if platform == 'linux' or platform == 'linux2':
        scan_cmd  = subprocess.Popen(['iwlist', interface, 'scan'])

    if platform == 'mac':
        scan_cmd = subprocess.Popen(['airport', '-s'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        scan_out, scan_err = scan_cmd.communicate()
        scan_out_data = {}
        scan_out_lines = str(scan_out).split("\\n")[1:-1]
        for each_line in scan_out_lines:
            split_line = [e for e in each_line.split(" ") if e != ""]
            print(split_line)
            line_data = {"SSID": split_line[0], "RSSI": int(split_line[2]), "channel": split_line[3], "HT": (split_line[4] == "Y"), "CC": split_line[5], "security": split_line[6]}
            scan_out_data[split_line[1]] = line_data
        return scan_out_data


def get_distance(ap_mac):
    nearby_aps = get_aps()
    if ap_mac not in nearby_aps.keys():
        print("Specified Access Point Not Found!")
        return -1 # Using -1 top indicate an error
    ap_rssi = nearby_aps[ap_mac]["RSSI"]
    print(ap_rssi)
    distance = -log10(3*((ap_rssi + 81)**9.9)) + 19.7 # Replace this with your equation
    return distance



if __name__ == "__main__":
    main()