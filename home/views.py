from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def main_page(self, request):
    return HttpResponse('TEST', content_type='text/plain')