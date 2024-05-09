from django.urls import path
from love import views
app_name='user'
urlpatterns = [
    path("welcome",views.welcome,name='welcome'),
    path("store_user",views.store_user,name='store_user'),
    path("data_leak",views.data_leak),
]