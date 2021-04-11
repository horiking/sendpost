from . import views
from django.urls import path


app_name = "sendmail"
urlpatterns = [
    path('', views.index),
    path('<int:mail_id>/', views.singel_mail, name ="detail"),
    path('all', views.all_mails),
]