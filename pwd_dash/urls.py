from django.urls import path,include

from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
]