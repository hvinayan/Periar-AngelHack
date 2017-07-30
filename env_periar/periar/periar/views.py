from django.http import HttpResponse
import random

def hello_world (request):
    return HttpResponse("Testing 123")
def root_page (request):
    return HttpResponse("Periar Root")