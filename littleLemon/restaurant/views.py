from django.shortcuts import render, HttpResponse
import os
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