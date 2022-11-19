from win32wifi.Win32NativeWifiApi import *
from win32wifi.Win32Wifi import getWirelessInterfaces
from win32wifi.Win32Wifi import WirelessNetworkBss


class GetRSSiBss(WirelessNetworkBss):
    def __init__(self, ifaces) -> None:
        WirelessNetworkBss.__init__(self, ifaces)
    
    def get_rssi(self):
        return self.rssi



def get_wirelessInfo():
    ifaces = getWirelessInterfaces()
    
    for iface in ifaces:
        # print(iface)
        guid = iface.guid
        bsss = get_rssi(iface)
        trigger = 0
        scan_out_data = {}
        for bs in bsss:
            trigger += 1
            scan_out_data[f'Address{trigger}'] = {
                "ap_mac": bs.bssid,
                "RSSI": bs.get_rssi()
            }
    return scan_out_data



def get_rssi(wireless_interface):
    networks = []
    handle = WlanOpenHandle()
    bss_list = WlanGetNetworkBssList(handle, wireless_interface.guid)
    # Handle the WLAN_BSS_LIST pointer to get a list of WLAN_BSS_ENTRY
    # structures.
    data_type = bss_list.contents.wlanBssEntries._type_
    num = bss_list.contents.NumberOfItems
    bsss_pointer = addressof(bss_list.contents.wlanBssEntries)
    bss_entries_list = (data_type * num).from_address(bsss_pointer)
    for bss_entry in bss_entries_list:
        networks.append(GetRSSiBss(bss_entry))
    WlanFreeMemory(bss_list)
    WlanCloseHandle(handle)
    return networks



if __name__ == "__main__":
    get_wirelessInfo()