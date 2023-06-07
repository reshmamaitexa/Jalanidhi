from rest_framework import serializers
from .models import Log, consumer,meter_reader,subadmin,panchayath_details,notification,complaintRegister, Complaints_Replay, connection_details, meter_reading, payment

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class consumerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumer
        fields = '__all__'
        def Create(self,validated_date):
            return consumer.objects.Create(**validated_date)        

class subadminRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = subadmin
        fields = '__all__'
        def Create(self,validated_date):
            return subadmin.objects.Create(**validated_date)   

class meter_readerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = meter_reader
        fields = '__all__'
        def Create(self,validated_date):
            return meter_reader.objects.Create(**validated_date) 

class panchayath_detailsRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = panchayath_details
        fields = '__all__'
        def Create(self,validated_date):
            return panchayath_details.objects.Create(**validated_date) 


class raeding_paymentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'
        def Create(self,validated_date):
            return payment.objects.Create(**validated_date)      


class complaintRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaints_Replay
        fields = '__all__'
        def Create(self,validated_date):
            return Complaints_Replay.objects.Create(**validated_date)       

class meter_readingRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = meter_reading
        fields = '__all__'
        def Create(self,validated_date):
            return meter_reading.objects.Create(**validated_date) 

class notificationRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = notification
        fields = '__all__'        

class connection_detailsRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = connection_details
        fields = '__all__'
        def Create(self,validated_date):
            return connection_details.objects.Create(**validated_date)       

            
# class service_chargeRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = service_charge
#         fields = '__all__'
#         def Create(self,validated_date):
#             return service_charge.objects.Create(**validated_date)                                                     