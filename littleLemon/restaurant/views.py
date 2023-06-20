from django.shortcuts import render, HttpResponse
import os
from rest_framework.generics import *
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.
def index(request):
  return render(request, 'index.html', {})

def staticfiles(request,name):
  print(name)
  try:
    with open(os.path.join(os.path.dirname(__file__),'static/restaurant/'+name),'rb') as f:
      return HttpResponse(f.read(),content_type="image/jpeg")
  except IOError:
    return HttpResponse(request,code=404)

class BookingViewSet(ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer

class MenuItemsView(ListCreateAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuSerializer

"""
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 
"""
