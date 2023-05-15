from temperature.models import Data, Temperature
from rest_framework import serializers
import time
  

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = [
            'data'
        ]
    # def validate_data(self, value):
    #     # Split the data string on the colon character
    #     data_fields = value.split(":")
    #     # Check if the data string has the correct format
    #     if len(data_fields) != 4:
    #         raise serializers.ValidationError("Data not correctly formatted!")
    #     try:
    #         self.device_id = int(data_fields[0])
    #     except:
    #         raise serializers.ValidationError("Device id is not an integer")
    #     try:
    #         self.epoch_ms = int(data_fields[1])
    #     except: 
    #         raise serializers.ValidationError("Epoch is not correctly formatted!")
    #     try:
    #         self.temperature = float(data_fields[3])
    #     except:
    #         raise serializers.ValidationError("Temperature is not correctly formatted!")
    #     try:
    #         self.temperature_string = str(data_fields[2])
    #     except:
    #         raise serializers.ValidationError("Temperature string should 'Temperature'")
    #     return value

    

