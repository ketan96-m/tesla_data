import json
import time

def parse_data_string(data_string):
    # Split the data string on the colon character
    data_fields = data_string.split(":")

    # Check if the data string has the correct format
    if len(data_fields) != 4:
        return None
    
    # Get the device ID, epoch MS, temperature, and temperature label
    try:
        device_id = int(data_fields[0])
        epoch_ms = int(data_fields[1])
        temperature = float(data_fields[3])
        temperature_string = str(data_fields[2])
    except:
        return None
    
    if temperature_string!="'Temperature'":
        return None

    # Check if the temperature is at or over 90 degrees
    if temperature >= 90:
        # print(epoch_ms)
        return {
            "overtemp": True,
            "device_id": device_id,
            "formatted_time": time.strftime(r"%Y/%m/%d %H:%M:%S", time.gmtime(epoch_ms/1000))
        }
    
    # Otherwise, the temperature is not over 90 degrees
    return {
        "overtemp": False
    }
    