from django.contrib import admin
from .models import Log,consumer,subadmin,meter_reader, panchayath_details, Complaints_Replay, connection_details, notification, payment

# Register your models here.

admin.site.register(Log)
admin.site.register(consumer)
admin.site.register(subadmin)
admin.site.register(meter_reader)
admin.site.register(panchayath_details)
admin.site.register(Complaints_Replay)
admin.site.register(connection_details)
admin.site.register(notification)
admin.site.register(payment)