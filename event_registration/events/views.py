from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event , Registration
from .serializers import EventSerializer , RegistrationSerializer
from django.shortcuts import get_object_or_404
# Create your views here.


@api_view(['GET'])
def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def event_detail(request , event_id):
    event = get_object_or_404(Event,id=event_id)
    serializer = EventSerializer(event)
    return Response(serializer.data)

@api_view(['POST'])
def register_event(request):
    user = request.user
    event_id = request.data.get('event_id')

    if not event_id:
        return Response({'error': 'event_id is required.'}, status=400)

    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
          return Response({'error': 'Event not found.'}, status=404)
    
    if Registration.objects.filter(user=user , event=event).exists():
        return Response({'error': "Already registered."}, status=400)
    
    registration = Registration.objects.create(user=user , event = event)
    serializer = RegistrationSerializer(registration)
    return Response(serializer.data,status=201)



@api_view(['GET'])
def my_registrations(request):
    registrations = Registration.objects.filter(user=request.user)
    serializer = RegistrationSerializer(registrations,many = True)
    return Response(serializer.data)


@api_view(['DELETE'])
def cancel_registration(request, registration_id):
    try:
        registration = Registration.objects.get(id=registration_id)
        registration.delete()
        return Response({'message': 'Registration cancelled successfully.'}, status=204)
    except Registration.DoesNotExist:
        return Response({'error': 'Registration not found.'}, status=404)
