from django.conf.urls import url 
from . import views 
urlpatterns=[
	url(r'^$',views.message_to_user,name="message_to_user"),  
	]