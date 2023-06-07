from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from jalanidhiapp.models import consumer, meter_reader, subadmin, panchayath_details, Complaints_Replay, connection_details, notification, payment
from jalanidhiapp import models
# Create your views here.


def dashboard(request):
    return render(request,'dashboard.html')

def Add_notification(request):
    return render(request,'Add_notification.html')

def Consumer_registration(request):
    data=consumer.objects.all()
    print(data)
    return render(request,'Consumer_registration.html',{"data":data})

def Due_report(request):
    return render(request,'Due_report.html')

def Reader_registration(request):
    data=meter_reader.objects.all()
    return render(request,'Reader_registration.html',{"data":data})

def Sud_admin_registration(request):
    data=subadmin.objects.all()
    return render(request,'Sub_admin_registration.html',{"data":data})

def View_area(request):
    data=panchayath_details.objects.all()
    return render(request,'View_area.html',{"data":data})

def View_complaint(request):
    data=Complaints_Replay.objects.all()
    return render(request,'View_complaint.html',{"data":data})


def admin_single_complaints(request,id):
    Data = Complaints_Replay.objects.get(id=id)
    return render(request,'admin_replay_complaint.html',{'Data':Data})

def admin_add_replay(request,id):
    if request.method=="POST":
        add=Complaints_Replay.objects.get(id=id)
        add.replay=request.POST["replay"]
        add.complaint_status="1"
        add.save()
        return redirect("View_complaint")


def View_connection(request):
    data=connection_details.objects.all()
    print(data)
    return render(request,'View_connection.html',{"data":data})

def View_payment(request):
    data=payment.objects.all()
    return render(request,'View_payment.html',{"data":data})



def admin_add_notification(request):
    if request.method == 'POST':
        notification = request.POST.get('notification')
        notification_date = request.POST.get('notification_date')
        notification_time = request.POST.get('notification_time')
        notification_status = '0'
        NotiDetails = models.notification(notification=notification, notification_date=notification_date,notification_time=notification_time,notification_status=notification_status)
        NotiDetails.save()
            
        return redirect('View_Notification')
    else:
        return render(request, 'Add_notification.html')



def View_Notification(request):
    data = notification.objects.all()
    return render(request,'admin_view_notification.html',{'data':data})