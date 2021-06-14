from django.urls import path
from . import views, HoDViews

app_name = 'sm_ap'

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('', views.show_login_page, name='login'),
    path('get_user_details/', views.get_user_details, name='get_user_details'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('test/', views.test, name='test'),
    path('admin_home/', HoDViews.Admin_home, name='admin_home'),
    path('add_staff/', HoDViews.add_staff, name='add_staff'),
]
