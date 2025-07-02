from django.urls import path
from .views import event_list , event_detail , register_event , my_registrations , cancel_registration



urlpatterns = [
    path('events/',event_list,name='event-list'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('register/', register_event,name='register-event'),
    path('my-registrations/',my_registrations,name="my-registrations"),
     path('cancel/<int:registration_id>/', cancel_registration, name='cancel-registration')
]   