from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from.models import Log,consumer,panchayath_details, subadmin, meter_reader, connection_details, notification, meter_reading, payment, Complaints_Replay
from jalanidhiapp.serializers import LoginUserSerializer,consumerRegisterSerializer,subadminRegisterSerializer,meter_readerRegisterSerializer,panchayath_detailsRegisterSerializer,notificationRegisterSerializer,complaintRegisterSerializer, connection_detailsRegisterSerializer, notificationRegisterSerializer, meter_readingRegisterSerializer, raeding_paymentRegisterSerializer


class consumerRegisterAPIView(GenericAPIView):
    serializer_class=consumerRegisterSerializer
    serializer_class_login=LoginUserSerializer

    def post(self,request):
        login_id=""
        consumer_name=request.data.get("name")
        house_name = request.data.get("house_name")
        dob = request.data.get("dob")
        house_no = request.data.get("house_no")
        aadhar_no= request.data.get("aadhar_no")
        email =request.data.get("email")
        gender= request.data.get("gender")
        pin_code = request.data.get("pin_code")
        phone_no = request.data.get("phone_no")
        panchayath_type = request.data.get("panchayath_type")
        panchayath_name = request.data.get("panchayath_name")
        ward_no= request.data.get("ward_no")
        category =request.data.get("category")
        category_proof =request.data.get("category_proof")
        username= request.data.get("username")
        password= request.data.get("password")
        role = 'Consumer'
        Consumerstatus='0'

        if(Log.objects.filter(username=username)):
            return Response({'message':'Duplicate username found'},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login=self.serializer_class_login(data={'username':username,'password':password,'role':role})
        if serializer_login.is_valid():
            log=serializer_login.save()
            login_id=log.id
            print(login_id)
        serializer=self.serializer_class(data={'name':consumer_name,'house_name':house_name,'dob':dob,'house_no':house_no,'aadhar_no':aadhar_no,'email':email,'gender':gender,'pin_code':pin_code,'phone_no':phone_no,'panchayath_type':panchayath_type,'panchayath_name':panchayath_name,'ward_no':ward_no,'category':category,'category_proof':category_proof,'login_id':login_id,'status':Consumerstatus,'role':role,})
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'Consumer registered successfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)

class LoginUsersAPIView(GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request):
        u_id=''
        username = request.data.get('username')
        password = request.data.get('password')
        # role = request.data.get('role')
        logreg = Log.objects.filter(username=username, password=password)
        if (logreg.count()>0):
            read_serializer = LoginUserSerializer(logreg, many=True)
            for i in read_serializer.data:
                id = i['id']
                print(id)
                role = i['role']

                regdata=consumer.objects.all().filter(login_id=id).values()
                print(regdata)
                for i in regdata:
                     u_id = i['id']
                     l_status=i['status']
                     category=i['category']
                     print(u_id)

                regdata=subadmin.objects.all().filter(subadmin_loginid=id).values()
                print(regdata)
                for i in regdata:
                     u_id = i['id']
                     l_status = i['status']
                     print(l_status)
                     print(u_id)
                    
                regdata=meter_reader.objects.all().filter(meter_reader_loginid=id).values()
                print(regdata)
                for i in regdata:
                     u_id = i['id']
                     l_status = i['status']
                     print(l_status)
                     print(u_id)
                
            return Response({'data':{'login_id':id,'username':username,'password':password,'role':role,'user_id':u_id,'l_status':l_status,'category':category},'success': True, 'message':'Logged in successfully'}, status=status.HTTP_200_OK)       
        else:
            return Response({'data':'username or password is invalid', 'success': False, }, status = status.HTTP_400_BAD_REQUEST)



class subadminRegisterAPIView(GenericAPIView):
    serializer_class=subadminRegisterSerializer
    serializer_class_login=LoginUserSerializer

    def post(self,request):
        login_id=""
        subadmin_name=request.data.get("subadmin_name")
        subadmin_district = request.data.get("subadmin_district")
        subadmin_city = request.data.get("subadmin_city")
        subadmin_dob = request.data.get("subadmin_dob")
        subadmin_pincode= request.data.get("subadmin_pincode")
        subadmin_phoneno =request.data.get("subadmin_phoneno")
        subadmin_email= request.data.get("subadmin_email")
        subadmin_gender = request.data.get("subadmin_gender")
        username= request.data.get("username")
        password= request.data.get("password")
        role = 'Subadmin'
        subadminstatus='0'

        if(Log.objects.filter(username=username)):
            return Response({'message':'Duplicate username found'},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login=self.serializer_class_login(data={'username':username,'password':password,'role':role})
        if serializer_login.is_valid():
            log=serializer_login.save()
            login_id=log.id
            print(login_id)
        serializer=self.serializer_class(data={'subadmin_name':subadmin_name,'subadmin_district':subadmin_district,'subadmin_city':subadmin_city,'subadmin_dob':subadmin_dob,'subadmin_pincode':subadmin_pincode,'subadmin_phoneno':subadmin_phoneno,'subadmin_email':subadmin_email,'subadmin_gender':subadmin_gender,'subadmin_loginid':login_id,'status':subadminstatus,'role':role,})
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'subadmin registered successfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)


class meter_readerRegisterAPIView(GenericAPIView):
    serializer_class=meter_readerRegisterSerializer
    serializer_class_login=LoginUserSerializer

    def post(self,request):
        login_id=""
        meter_reader_name=request.data.get("meter_reader_name")
        meter_reader_district = request.data.get("meter_reader_district")
        meter_reader_city = request.data.get("meter_reader_city")
        meter_reader_dob = request.data.get("meter_reader_dob")
        meter_reader_destination = request.data.get("meter_reader_destination")
        meter_reader_pincode= request.data.get("meter_reader_pincode")
        meter_reader_phoneno =request.data.get("meter_reader_phoneno")
        meter_reader_email= request.data.get("meter_reader_email")
        meter_reader_gender = request.data.get("meter_reader_gender")
        username= request.data.get("username")
        password= request.data.get("password")
        role = 'reader'
        meter_readerstatus='0'

        if(Log.objects.filter(username=username)):
            return Response({'message':'Duplicate username found'},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login=self.serializer_class_login(data={'username':username,'password':password,'role':role})
            print(serializer_login)
        if serializer_login.is_valid():
            log=serializer_login.save()
            print(log)
            login_id=log.id
            print(login_id)
        serializer=self.serializer_class(data={'meter_reader_name':meter_reader_name,'meter_reader_district':meter_reader_district,'meter_reader_city':meter_reader_city,'meter_reader_dob':meter_reader_dob,'meter_reader_destination':meter_reader_destination,'meter_reader_pincode':meter_reader_pincode,'meter_reader_phoneno':meter_reader_phoneno,'meter_reader_email':meter_reader_email,'meter_reader_gender':meter_reader_gender,'meter_reader_loginid':login_id,'status':meter_readerstatus,'role':role})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'meter reader registered successfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)

class Get_ConsumerAPIView(GenericAPIView):
    serializer_class = consumerRegisterSerializer
    def get(self, request):
        queryset = consumer.objects.all()
        if (queryset.count()>0):
            serializer = consumerRegisterSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message':'data get', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class SingleConsumerAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = consumer.objects.get(pk=id)
        serializer = consumerRegisterSerializer(queryset)
        return Response({'data': serializer.data, 'message':'single consumer data', 'success':True}, status=status.HTTP_200_OK)



class Update_ConsumerAPIView(GenericAPIView):
    serializer_class = consumerRegisterSerializer
    def put(self, request, id):
        queryset = consumer.objects.get(pk=id)
        print(queryset)
        serializer = consumerRegisterSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'updated successfully', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'Something Went Wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)





class Get_MeterReaderAPIView(GenericAPIView):
    serializer_class = meter_readerRegisterSerializer
    def get(self, request):
        queryset = meter_reader.objects.all()
        if (queryset.count()>0):
            serializer = meter_readerRegisterSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message':'data get', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class SingleMeterReaderAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = meter_reader.objects.get(pk=id)
        serializer = meter_readerRegisterSerializer(queryset)
        return Response({'data': serializer.data, 'message':'single meter reader data', 'success':True}, status=status.HTTP_200_OK)



class Update_MeterReaderAPIView(GenericAPIView):
    serializer_class = meter_readerRegisterSerializer
    def put(self, request, id):
        queryset = meter_reader.objects.get(pk=id)
        print(queryset)
        serializer = meter_readerRegisterSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'updated successfully', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'Something Went Wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)



class Get_SubadminAPIView(GenericAPIView):
    serializer_class = subadminRegisterSerializer
    def get(self, request):
        queryset = subadmin.objects.all()
        if (queryset.count()>0):
            serializer = subadminRegisterSerializer(queryset, many=True)
            
            return Response({'data': serializer.data, 'message':'data get', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class SingleSubadminAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = subadmin.objects.get(pk=id)
        serializer = subadminRegisterSerializer(queryset)
        return Response({'data': serializer.data, 'message':'single sub admin data', 'success':True}, status=status.HTTP_200_OK)



class Update_SubadminAPIView(GenericAPIView):
    serializer_class = subadminRegisterSerializer
    def put(self, request, id):
        queryset = subadmin.objects.get(pk=id)
        print(queryset)
        serializer = subadminRegisterSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'updated successfully', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'Something Went Wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)




class panchayath_detailsAPIView(GenericAPIView):
    serializer_class=panchayath_detailsRegisterSerializer

    def post(self,request):
        sub_admin=request.data.get("sub_admin")
        meter_reader=request.data.get("meter_reader")
        panchayath_type=request.data.get("panchayath_type")
        panchayath_name = request.data.get("panchayath_name")
        ward_no = request.data.get("ward_no")
        panchayath_status='0'

        serializer=self.serializer_class(data={'panchayath_type':panchayath_type,'panchayath_name':panchayath_name,'ward_no':ward_no,'sub_admin':sub_admin,'meter_reader':meter_reader,'panchayath_status':panchayath_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'Panchayath details entered successfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)


class Get_AreaAPIView(GenericAPIView):
    serializer_class = panchayath_detailsRegisterSerializer
    def get(self, request):
        queryset = panchayath_details.objects.all()
        if (queryset.count()>0):
            serializer = panchayath_detailsRegisterSerializer(queryset, many=True)
            print(serializer)
            for i in serializer.data:
                sub_name=i['sub_admin']
                meter_name=i['meter_reader']
                pan_type=i['panchayath_type']
                pan_name=i['panchayath_name']
                ward_no=i['ward_no']
                
                data= meter_reader.objects.all().filter(id=meter_name).values()
                for i in data:
                    m_name=i['meter_reader_name']

                data= subadmin.objects.all().filter(id=meter_name).values()
                for i in data:
                    s_name=i['subadmin_name']

            return Response({'data': {'sub_admin':s_name,'meter_reader':m_name,'panchayath_type':pan_type,'panchayath_name':pan_name,'ward_no':ward_no}, 'message':'data get', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class SingleAreaAPIView(GenericAPIView):
    def get(self, request, id):
        queryset = panchayath_details.objects.get(pk=id)
        serializer = panchayath_detailsRegisterSerializer(queryset)
        return Response({'data': serializer.data, 'message':'single area data', 'success':True}, status=status.HTTP_200_OK)



class Update_AreaAPIView(GenericAPIView):
    serializer_class = panchayath_detailsRegisterSerializer
    def put(self, request, id):
        queryset = panchayath_details.objects.get(pk=id)
        print(queryset)
        serializer = panchayath_detailsRegisterSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'updated successfully', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'Something Went Wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)



class MeteReaderSingleAreaAPIView(GenericAPIView):
    def get(self, request, id):
        qset = meter_reader.objects.all().filter(pk=id).values()
        for i in qset:
            u_id=i['id']

        data=panchayath_details.objects.all().filter(meter_reader=u_id).values()
        print(data)
        return Response({'data':data, 'message':'meter reader single area data', 'success':True}, status=status.HTTP_200_OK)



class ConsumerComplaintsAndReplayAPIView(GenericAPIView):
    serializer_class = complaintRegisterSerializer

    def post(self, request):
        con = request.data.get('consumer')
        complaint = request.data.get('complaint')
        date = request.data.get('date')
        complaint_status="0"

        data=consumer.objects.all().filter(id=con).values()
        for i in data:
            name=i['name']


        serializer = self.serializer_class(data= {'consumer':con, 'consumer_name':name, 'complaint':complaint,'date':date,'complaint_status':complaint_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Complaints Added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)



class ComplaintAndReplayPIView(GenericAPIView):
    def get(self, request, id):
        queryset = consumer.objects.all().filter(pk=id).values()
        print(queryset)
        for i in queryset:
            con = i['id']
            print('///////////',con)
        instance = Complaints_Replay.objects.all().filter(consumer=con).values()
        print("======",instance)
        # serializer = complaintRegisterSerializer(instance)
        return Response({'data': instance, 'message':'complaint  data', 'success':True}, status=status.HTTP_200_OK)



class ConsumerConnectionAPIView(GenericAPIView):
    serializer_class = connection_detailsRegisterSerializer

    def post(self, request):
        consumer = request.data.get('consumer')
        category = request.data.get('category')
        connection_amt = request.data.get('connection_amt')
        panchayath_type=request.data.get('panchayath_type')
        panchayath_name=request.data.get('panchayath_name')
        ward_no=request.data.get('ward_no')
        connection_status="0"
        
        if category == "Bpl":
            return Response({'data':serializer.data, 'message':'Free Connection', 'success':True}, status = status.HTTP_201_CREATED)

        serializer = self.serializer_class(data= {'consumer':consumer, 'category':category, 'connection_amt':connection_amt,'panchayath_type':panchayath_type,'panchayath_name':panchayath_name,'ward_no':ward_no,'connection_status':connection_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Connection Added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)



class SubAdminApprove_ConnectionAPIView(GenericAPIView):
    def post(self, request, id):
        serializer_class = connection_detailsRegisterSerializer
        contn = connection_details.objects.get(pk=id)
        contn.connection_status = 1
        contn.save()
        serializer = serializer_class(contn)
        return Response({'data':serializer.data,'message':'SubAdmin Approved Connection', 'success':True}, status=status.HTTP_200_OK)


class Delete_ConnectionAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = connection_details.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Deleted successfully', 'success':True}, status=status.HTTP_200_OK)



class Get_ConnectionAPIView(GenericAPIView):
    serializer_class = connection_detailsRegisterSerializer
    def get(self, request):
        queryset = connection_details.objects.all()
        print(queryset)
        if (queryset.count()>0):
            serializer = connection_detailsRegisterSerializer(queryset, many=True)
         
            print(serializer)
            # for i in serializer.data:
            #     con_name=i['consumer']
            #     con_amt=i['connection_amt']
                
                # data= consumer.objects.all().filter(id=con_name).values()
                # for i in data:
                #     name=i['name']


            return Response({'data': serializer.data, 'message':'data get', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class Get_NotificationAPIView(GenericAPIView):
    serializer_class = notificationRegisterSerializer
    def get(self, request):
        queryset = notification.objects.all()
        if (queryset.count()>0):
            serializer = notificationRegisterSerializer(queryset, many=True)
            
            return Response({'data': serializer.data, 'message':'data get', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)




class meter_reading_detailsAPIView(GenericAPIView):
    serializer_class=meter_readingRegisterSerializer

    def post(self,request):
        consumer=request.data.get("consumer")
        meter_reader=request.data.get("meter_reader")
        current_meter_reading=request.data.get("current_meter_reading")
        meter_reading_date = request.data.get("meter_reading_date")
        meter_reading_duedate = request.data.get("meter_reading_duedate")
        meter_reading_price = request.data.get("meter_reading_price")
        meter_reading_status='0'

        serializer=self.serializer_class(data={'consumer':consumer,'meter_reader':meter_reader,'current_meter_reading':current_meter_reading,'meter_reading_date':meter_reading_date,'meter_reading_duedate':meter_reading_duedate,'meter_reading_price':meter_reading_price, 'meter_reading_status':meter_reading_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'Panchayath details entered successfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)


class ConsumerMeterReadingPIView(GenericAPIView):
    def get(self, request, id):
        consumers=""
        queryset = consumer.objects.all().filter(pk=id).values()
        print(queryset)
        for i in queryset:
            consumers = i['id']
            print('///////////',consumers)
        instance = meter_reading.objects.all().filter(consumer=consumers).values()
        
        return Response({'data': instance, 'message':'Meter Reading Data  data', 'success':True}, status=status.HTTP_200_OK)



class meter_reading_paymentdetailsAPIView(GenericAPIView):
    serializer_class=raeding_paymentRegisterSerializer

    def post(self,request):
        consumer=request.data.get("consumer")
        reading_amount=request.data.get("reading_amount")
        read_status='0'

        serializer=self.serializer_class(data={'consumer':consumer,'reading_amount':reading_amount, 'read_status':read_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'payment successfull','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)


class Get_paymentAPIView(GenericAPIView):
    serializer_class = raeding_paymentRegisterSerializer
    def get(self, request):
        queryset = payment.objects.all()
        if (queryset.count()>0):
            serializer = raeding_paymentRegisterSerializer(queryset, many=True)
            
            return Response({'data': serializer.data, 'message':'data get', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available', 'success':False}, status=status.HTTP_400_BAD_REQUEST)





























# class connection_paymentAPIView(GenericAPIView):
#     serializer_class=connection_paymentSerializer

#     def post(self,request):
#         connection_amount=request.data.get("connection_amount")
#         connection_payment_type = request.data.get("connection_payment_type")
#         connection_date = request.data.get("connection_date")
#         connection_status='0'

#         serializer=self.serializer_class(data={'connection_amount':connection_amount,'connection_payment_type':connection_payment_type,'connection_date':connection_date,'connection_status':connection_status})
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data,'message':'Connection payment done successfully','success':True},status=status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)

class consumer_complaintAPIView(GenericAPIView):
    serializer_class=complaintRegisterSerializer

    def post(self,request):
        consumer=request.data.get("consumer")
        complaint=request.data.get("complaint")
        complaint_time = request.data.get("complaint_time")
        complaint_date = request.data.get("complaint_date")
        complaint_status='0'

        serializer=self.serializer_class(data={'complaint':complaint,'complaint_time':complaint_time,'complaint_date':complaint_date,'consumer':consumer,'complaint_status':complaint_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'Complaint sent successfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)

# class meter_readingAPIView(GenericAPIView):
#     serializer_class=meter_readingSerializer

#     def post(self,request):
#         current_meter_reading=request.data.get("current_meter_reading")
#         previous_meter_reading = request.data.get("previous_meter_reading")
#         meter_reading_date = request.data.get("meter_reading_date")
#         meter_reading_status='0'

#         serializer=self.serializer_class(data={'current_meter_reading':current_meter_reading,'previous_meter_reading':previous_meter_reading,'meter_reading_date':meter_reading_date,'status':meter_reading_status})
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data,'message':'Meter reading entered successfully','success':True},status=status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)

class notificationAPIView(GenericAPIView):
    serializer_class=notificationRegisterSerializer

    def post(self,request):
        notification=request.data.get("notification")
        notification_date = request.data.get("notification_date")
        notification_time = request.data.get("notification_time")
        users_type = request.data.get("users_type")
        notification_status='0'

        serializer=self.serializer_class(data={'notification':notification,'notification_date':notification_date,'notification_time':notification_time,'users_type':users_type,'notification_status':notification_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'Notification entered successfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)

# class connection_detailsAPIView(GenericAPIView):
#     serializer_class=connection_detailsSerializer

#     def post(self,request):
#         connection_no=request.data.get("connection_no")
#         connection_applied_date = request.data.get("connection_applied_date")
#         connection_established_date = request.data.get("connection_established_date")
#         connection_status='0'

#         serializer=self.serializer_class(data={'connection_no':connection_no,'connection_applied_date':connection_applied_date,'connection_established_date':connection_established_date,'status':connection_status})
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data,'message':'Connection gained successfully','success':True},status=status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)

# class service_chargeAPIView(GenericAPIView):
#     serializer_class=service_chargeSerializer

#     def post(self,request):
#         service_amount=request.data.get("service_amount")
#         service_due_report = request.data.get("service_due_report")
#         service_date = request.data.get("service_date")
#         service_status='0'

#         serializer=self.serializer_class(data={'service_amount':service_amount,'service_due_report':service_due_report,'service_date':service_date,'status':service_status})
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data,'message':'service payment submit successfully','success':True},status=status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors,'message':'failed','success':False},status=status.HTTP_400_BAD_REQUEST)


        







