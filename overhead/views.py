from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shelf_stock(request):
    return HttpResponse('Stock the shelf with overhead!')

def shelf_item(request, item_id):
    """An item of the warehouse"""
    return HttpResponse(f"Looking at {item_id}")

def shelf_search(request, term):
    """Search the shop."""
    return HttpResponse(f"Searching for {term}")

def shelf_test(request, arg):
    """Search the shop"""
    return HttpResponse(f"Testing for {arg}")