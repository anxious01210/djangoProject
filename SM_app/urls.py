from django.urls import path
from . import views

app_name = 'sm_ap'

urlpatterns = [
    path('', views.show_login_page, name='login'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('get_user_details/', views.get_user_details, name='get_user_details'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('demo/', views.demo, name='demo'),
]
