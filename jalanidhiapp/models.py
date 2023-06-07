from django.db import models


# Create your models here.
class Log(models.Model):
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20,unique=True)
    role=models.CharField(max_length=10)
    def __str__(self):
        return self.username

class consumer(models.Model):
    name = models.CharField(max_length=20)
    house_name = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    house_no = models.CharField(max_length=10)
    aadhar_no= models.CharField(max_length=11)
    email = models.CharField(max_length=20)
    gender= models.CharField(max_length=20)
    pin_code = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)
    panchayath_type = models.CharField(max_length=20)
    panchayath_name = models.CharField(max_length=20)
    ward_no= models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    category_proof = models.ImageField(upload_to='images',blank=True,null=True)
    login_id = models.OneToOneField(Log,on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class subadmin(models.Model):
    subadmin_name = models.CharField(max_length=20)
    subadmin_district = models.CharField(max_length=20)
    subadmin_city= models.CharField(max_length=20)
    subadmin_dob = models.CharField(max_length=20)
    subadmin_pincode =models.IntegerField()
    subadmin_phoneno= models.IntegerField()
    subadmin_email = models.CharField(max_length=20)
    subadmin_gender= models.CharField(max_length=20)
    subadmin_loginid = models.OneToOneField(Log,on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.subadmin_name


class meter_reader(models.Model):
    meter_reader_name = models.CharField(max_length=20)
    meter_reader_district = models.CharField(max_length=20)
    meter_reader_city= models.CharField(max_length=20)
    meter_reader_dob = models.CharField(max_length=20)
    meter_reader_destination = models.CharField(max_length=20)
    meter_reader_pincode = models.IntegerField()
    meter_reader_phoneno= models.IntegerField()
    meter_reader_email = models.CharField(max_length=20)
    meter_reader_gender= models.CharField(max_length=20)
    meter_reader_loginid = models.OneToOneField(Log,on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.meter_reader_name

class panchayath_details(models.Model):
    sub_admin = models.ForeignKey(subadmin,on_delete=models.CASCADE)
    meter_reader = models.ForeignKey(meter_reader,on_delete=models.CASCADE)
    panchayath_type = models.CharField(max_length=20)
    panchayath_name = models.CharField(max_length=20)
    ward_no = models.IntegerField()
    panchayath_status = models.CharField(max_length=20)


    def __str__(self):
        return self.panchayath_name

class payment(models.Model):
    consumer = models.ForeignKey(consumer,on_delete=models.CASCADE)
    reading_amount = models.CharField(max_length=20)
    read_status = models.CharField(max_length=20)

class complaintRegister(models.Model):
    consumer = models.ForeignKey(consumer,on_delete=models.CASCADE)
    complaint = models.CharField(max_length=20)
    complaint_time = models.CharField(max_length=20)
    complaint_date= models.CharField(max_length=20)
    complaint_status = models.CharField(max_length=20)

class meter_reading(models.Model):
    consumer = models.ForeignKey(consumer,on_delete=models.CASCADE)
    meter_reader = models.ForeignKey(meter_reader,on_delete=models.CASCADE)
    current_meter_reading = models.CharField(max_length=20)
    meter_reading_date= models.CharField(max_length=20)
    meter_reading_duedate= models.CharField(max_length=20)
    meter_reading_price= models.CharField(max_length=20)
    meter_reading_status = models.CharField(max_length=20)

class Complaints_Replay(models.Model):
    consumer = models.ForeignKey(consumer,on_delete=models.CASCADE)
    consumer_name = models.CharField(max_length=500)
    complaint = models.CharField(max_length=500)
    date = models.DateField()
    replay= models.CharField(max_length=500,default='No Replay')
    complaint_status = models.CharField(max_length=10)

    def __str__(self):
        return self.replay



class notification(models.Model):
    notification = models.CharField(max_length=20)
    notification_date = models.DateField()
    notification_time= models.CharField(max_length=20)
    notification_status = models.CharField(max_length=20)


class connection_details(models.Model):
    consumer = models.ForeignKey(consumer,on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    connection_amt = models.IntegerField()
    panchayath_type=models.CharField(max_length=20)
    panchayath_name=models.CharField(max_length=20)
    ward_no=models.IntegerField()
    connection_status = models.CharField(max_length=50)

# class service_charge(models.Model):
#     service_amount = models.CharField(max_length=20)
#     service_charge_type = models.CharField(max_length=20)
#     service_due_report = models.CharField(max_length=20)
#     service_date= models.CharField(max_length=20)
#     service_status = models.CharField(max_length=20)


    

