from django.urls import path
from adminapp import views

urlpatterns = [
   
   path('', views.dashboard, name='dashboard'),
   path('Add_notification', views.Add_notification, name='Add_notification'),
   path('Consumer_registration', views.Consumer_registration, name='Consumer_registration'),
   path('Due_report', views.Due_report, name='Due_report'),
   path('Reader_registration', views.Reader_registration, name='Reader_registration'),
   path('Sud_admin_registration', views.Sud_admin_registration, name='Sud_admin_registration'),
   path('View_area', views.View_area, name='View_area'),
   path('View_complaint', views.View_complaint, name='View_complaint'),
   path('View_connection', views.View_connection, name='View_connection'),
   path('View_payment', views.View_payment, name='View_payment'),

   path('admin_single_complaints/<int:id>', views.admin_single_complaints, name='admin_single_complaints'),
   path('admin_add_replay/<int:id>', views.admin_add_replay, name='admin_add_replay'),
   
   path('admin_add_notification', views.admin_add_notification, name='admin_add_notification'),
   path('View_Notification', views.View_Notification, name='View_Notification'),


]