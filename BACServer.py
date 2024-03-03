import BAC0
from time import sleep
from datetime import datetime

def show_current_date_and_time():
    """顯示當前日期和時間"""
    current_date_and_time = datetime.now()
    print("當前日期和時間是：", current_date_and_time)

def get_bac0_device(device_info, BACnetwork):
    """根據給定的設備信息和BACnet網絡獲取BAC0設備"""
    print("正在獲取BAC0設備")
    name, vendor, address, device_id = device_info
    try:
        return BAC0.device(address, device_id, BACnetwork, poll=0, object_list=None)
    except Exception as e:
        print(f"獲取設備時出錯：{e}")
        return None

def discover_devices(bacnet, devices_list):
    """發現和處理BACnet設備"""
    bacnet.discover()
    devices = bacnet.devices
    print(f"發現的設備：{devices}")
    for device in devices:
        _, _, address, device_id = device
        device_key = f'{address}:{device_id}'
        print(device_key)
        bac_device = get_bac0_device(device, bacnet)
        if bac_device:
            print_device_points(bac_device)
        
def print_device_points(bac_device):
    """BAC0設備的點位信息"""
    points = bac_device.points
    print("---")
    for point in points:
        print(f"{point} - {str(point.lastValue)}")
    print("---")



if __name__ == "__main__":
    try:
        bacnet = BAC0.connect()
        devices_list = {}
        while True:
            show_current_date_and_time()
            discover_devices(bacnet, devices_list)
            sleep(5)  # 或者可以將這個值提取到一個配置變量中，以便根據需要調整
    except KeyboardInterrupt:
        print("手動中斷")
    except Exception as e:
        print(f"發生錯誤：{e}")
