from django.urls import path,include
from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('get-token', views.UserLogin.as_view(), name='get-token'),
    path('tn_state', views.TnState.as_view(), name='tn_state'),
    path('tn_district', views.TnDistrict.as_view(), name='tn_district'),
     path('tn_blocks', views.TnBlock.as_view(), name='tn_blocks'),
]