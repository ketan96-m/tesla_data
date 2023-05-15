from django.db import models

# Create your models here.

class Data(models.Model):
    data = models.CharField(max_length=100)


# class Errors(models.Model):
#     # errors = models.CharField(max_length=200)
#     errors = models.ListCharField(
#         base_field=models.CharField(max_length=100),
#         # size=6,
#         # max_length=(6 * 11),  # 6 * 10 character nominals, plus commas
#     )
    

class Temperature(models.Model):
    device_ID  = models.IntegerField()
    temperature = models.FloatField()
    epochMS = models.IntegerField()

