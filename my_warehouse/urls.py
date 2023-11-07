"""
URL configuration for my_warehouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from overhead.views import shelf_stock,shelf_item,shelf_search,shelf_test
from packages.views import wrap_packages,wrap_item,wrap_search, wrap_test



urlpatterns = [
    path("admin/", admin.site.urls),
    path('overhead/', shelf_stock),
    path('overhead/<int:item_id>/', shelf_item),
    path('overhead/<str:term>/', shelf_search),
    re_path('testoverhead/(.*)/', shelf_test),
    path('packages/', wrap_packages),
    path('packages/<int:item_id>/', wrap_item),
    path('packages/<str:term>/',wrap_search),
    re_path('testpackages/(.*)/', wrap_test)
]


