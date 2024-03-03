from time import sleep
import random
from BAC0.core.devices.local.object import ObjectFactory
from bacpypes.object import ScheduleObject
from bacpypes.primitivedata import Real
from BAC0 import lite, connect
from BAC0.core.devices.local.models import (
    analog_input,
    analog_output,
    binary_output,
    binary_input,
)

def_device = {
    # "ip": "127.0.0.1/24",
    # "port": 47808,
    "deviceId": "1110",
}

def defining_object(device):
    ObjectFactory.clear_objects()

    _new_objects = analog_input(
        instance=10,
        name="Frequency",
        properties={"units": "hertz"},
        description="Frequency",
        presentValue=18.0,
    )
    analog_input(
        instance=20,
        name="Barometer",
        properties={"units": "pascals"},
        description="Room Pressure",
        presentValue=19.0,
    )
    analog_input(
        instance=10,
        name="Humidity",
        properties={"units": "degreesCelsius"},
        description="Room Humidity",
        presentValue=21,
        relinquish_default=21
    )
    analog_input(
        instance=20,
        name="Temperature",
        properties={"units": "degreesCelsius"},
        description="Room Temperature",
        presentValue=20,
        relinquish_default=20
    )
    analog_output(
        instance=20,
        name="Gas resistence",
        properties={"units": "degreesCelsius"},
        description="Room two set point",
        presentValue=20,
        relinquish_default=20
    )
    binary_output(
        instance=10,
        name="RoomOneHeatingEnabled",
        description="Room one heating enabled",
        presentValue=True,
    )
    binary_output(
        instance=20,
        name="RoomTwoHeatingEnabled",
        description="Room two heating enabled",
        presentValue=True,
    )
    binary_input(
        instance=10,
        name="RoomOneRadiatorState",
        description="Room one radiator on/off",
        presentValue=False,
    )
    binary_input(
        instance=20,
        name="RoomTwoRadiatorState",
        description="Room two radiator on/off",
        presentValue=False,
    )

    return _new_objects.add_objects_to_application(device) 


# device = connect(ip=def_device["ip"], port=def_device["port"], deviceId=def_device["deviceId"])
device = connect(deviceId=def_device["deviceId"])

defining_object(device)

while True:
    device["Frequency"].presentValue = random.uniform(5, 100)
    device["Temperature"].presentValue = random.uniform(5, 100)

    print(f"Device {def_device['deviceId']} - Frequency: {device['Frequency'].presentValue}")
    print(f"Device {def_device['deviceId']} - Temperature: {device['Temperature'].presentValue}")
    print(f"Device {def_device['deviceId']} - Temperature: {device['Humidity'].presentValue}")
    print(" ")

    sleep(5)