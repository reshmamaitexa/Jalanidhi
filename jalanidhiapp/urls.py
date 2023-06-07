from django.urls import path
from jalanidhiapp import views

urlpatterns = [
   
   path('login_users', views.LoginUsersAPIView.as_view(), name='login_users'),

   path('consumer_register', views.consumerRegisterAPIView.as_view(), name='consumer_register'),

   path('subadmin_register', views.subadminRegisterAPIView.as_view(), name='subadmin_register'),

   path('meter_reader_register', views.meter_readerRegisterAPIView.as_view(), name='meter_reader_register'),

   path('panchayath_details', views.panchayath_detailsAPIView.as_view(), name='panchayath_details'),

   # path('connection_payment', views.connection_paymentAPIView.as_view(), name='connection_payment'),
   path('consumer_complaint', views.consumer_complaintAPIView.as_view(), name='consumer_complaintAPIView'),

   # path('meter_reading', views.meter_readingAPIView.as_view(), name='meter_reading'),
   # path('notification', views.notificationAPIView.as_view(), name='notification'),
   # path('connection_details', views.connection_detailsAPIView.as_view(), name='connection_details'),
   # path('service_charge', views.service_chargeAPIView.as_view(), name='service_charge'),


   path('all_consumer', views.Get_ConsumerAPIView.as_view(), name='all_consumer'),
   path('single_consumer/<int:id>', views.SingleConsumerAPIView.as_view(), name='single_consumer'),
   path('update_consumer/<int:id>', views.Update_ConsumerAPIView.as_view(), name='update_consumer'),


   path('all_meter_reader', views.Get_MeterReaderAPIView.as_view(), name='all_meter_reader'),
   path('single_meter_reader/<int:id>', views.SingleMeterReaderAPIView.as_view(), name='single_meter_reader'),
   path('update_meter_reader/<int:id>', views.Update_MeterReaderAPIView.as_view(), name='update_meter_reader'),


   path('all_subadmin', views.Get_SubadminAPIView.as_view(), name='all_subadmin'),
   path('single_subadmin/<int:id>', views.SingleAreaAPIView.as_view(), name='single_subadmin'),
   path('update_subadmin/<int:id>', views.Update_SubadminAPIView.as_view(), name='update_subadmin'),


   path('all_area', views.Get_AreaAPIView.as_view(), name='all_area'),
   path('single_area/<int:id>', views.SingleAreaAPIView.as_view(), name='single_area'),
   path('update_area/<int:id>', views.Update_AreaAPIView.as_view(), name='update_area'),


   path('meterreader_single_area/<int:id>', views.MeteReaderSingleAreaAPIView.as_view(), name='meterreader_single_area'),


   path('consumer_complaints', views.ConsumerComplaintsAndReplayAPIView.as_view(), name='consumer_complaints'),
   path('complaintsingle_view/<int:id>', views.ComplaintAndReplayPIView.as_view(), name='complaintsingle_view'),

   path('consumer_connection', views.ConsumerConnectionAPIView.as_view(), name='consumer_connection'),
   path('all_consumer_connection', views.Get_ConnectionAPIView.as_view(), name='all_consumer_connection'),
   path('consumer_connection_approve/<int:id>', views.SubAdminApprove_ConnectionAPIView.as_view(), name='consumer_connection_approve'),
   path('consumer_connection_reject/<int:id>', views.Delete_ConnectionAPIView.as_view(), name='consumer_connection_reject'),

   path('notification', views.Get_NotificationAPIView.as_view(), name='notification'),

   path('meter_reading', views.meter_reading_detailsAPIView.as_view(), name='meter_reading'),

   path('consumer_reading/<int:id>', views.ConsumerMeterReadingPIView.as_view(), name='consumer_reading'),

   path('meter_reading_payment', views.meter_reading_paymentdetailsAPIView.as_view(), name='meter_reading_payment'),

   path('reading_payment', views.Get_paymentAPIView.as_view(), name='reading_payment'),




   
]