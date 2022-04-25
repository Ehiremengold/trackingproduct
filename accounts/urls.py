from django.urls import path
from .views import login, register

app_name = "accounts"

urlpatterns = [
	path('login/', login, name='login'),
	path('create-account/', register, name='register')
]