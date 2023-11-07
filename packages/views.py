from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wrap_packages(request):
    return HttpResponse('Wrap boxes and packages.')

def wrap_item(request, item_id):
    """An item in the package."""
    return HttpResponse(f"Looking at {item_id}")

def wrap_search(request, term):
    """Search the package."""
    return HttpResponse(f"Searching for {term}")

def wrap_test(request, arg):
    """Search the package."""
    return HttpResponse(f"Testing for {arg}")