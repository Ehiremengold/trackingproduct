from django.urls import path
from .views import index, trackproduct, tracking, about, contact, service, covid, fleet, airfreight, oceanfreight, raillogistics, roadlogistics, warehousing

urlpatterns = [
	path('', index, name='home'),
	path('about/', about, name='about'),
	path('contact/', contact, name='contact'),
	path('service/', service, name='service'),
	path('covid/', covid, name='covid'),
	path('trackproduct/', trackproduct, name='trackproduct'),
	path('tracking/', tracking, name='tracking'),
	path('fleet/', fleet, name='fleet'),	
	path('airfreight/', airfreight, name='airfreight'),
	path('oceanfreight/', oceanfreight, name='oceanfreight'),
	path('raillogistics/', raillogistics, name='raillogistics'),
	path('roadlogistics/', roadlogistics, name='roadlogistics'),
	path('warehousing/', warehousing, name='warehousing'),
]
"""path('tracker/', tracker, name='tracker'),"""