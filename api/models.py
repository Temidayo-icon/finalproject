from django.db import models

class Reading(models.Model):
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
 def __str__(self):
        return f"Voltage: {self.voltage}V, Current: {self.current}A, Power: {self.power}W, Timestamp: {self.created_at}"