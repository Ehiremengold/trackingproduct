from django.db import models
from django.utils.crypto import get_random_string

CHOICES = (("Order Confirmed", "Order Confirmed"),
			("Picked Up By Courier", "Picked Up By Courier"), 
			("On The Way", "On The Way"),
			("Ready For Pickup", "Ready For Pickup"),
	)

paid_choices = (("Pending", "Pending"), 
				("Paid", "Paid")) 

class ShippedProduct(models.Model):
	tracking_id = models.CharField(default=get_random_string, max_length=23)
	product_image = models.ImageField(upload_to='product_image/')
	payment_status = models.CharField(choices=paid_choices, max_length=100)
	product_status = models.CharField(choices=CHOICES, max_length=100, default="Order Confirmed")
	product_name = models.CharField(max_length=250)
	shipment_origin = models.CharField(max_length=250)
	shipment_destination = models.CharField(max_length=250)
	transportation_type = models.CharField(max_length=250) #transport method
	shipment_product_details = models.CharField(max_length=250)
	shipment_weight = models.CharField(max_length=250)
	pickup_date = models.DateTimeField()
	scheduled_delivery_date = models.DateTimeField()
	#ShippersInformation
	shippers_full_name = models.CharField(max_length=250)
	shippers_phone_number = models.CharField(max_length=15)
	shippers_address = models.CharField(max_length=250)
	#ReceiversInformation
	receivers_full_name = models.CharField(max_length=250)
	receivers_phone_number = models.CharField(max_length=15)
	receivers_address = models.CharField(max_length=400)
	last_location = models.CharField(max_length=400)
	history_status = models.CharField(max_length=200)
	remarks = models.CharField(max_length=400)
	history_date = models.DateTimeField()
	last_location2 = models.CharField(blank=True, max_length=400)
	history_status2 = models.CharField(blank=True, max_length=200)
	remarks2 = models.CharField(blank=True, max_length=400)
	history_date2 = models.DateTimeField(blank=True, null=True)
	last_location3 = models.CharField(blank=True, max_length=400)
	history_status3 = models.CharField(blank=True, max_length=200)
	remarks3 = models.CharField(blank=True, max_length=400)
	history_date3 = models.DateTimeField(blank=True, null=True)

	
	def __str__(self):
		return self.tracking_id

class YourMessage(models.Model):
	name = models.CharField(max_length=300)
	email = models.EmailField()
	subject = models.CharField(max_length=200)
	message = models.TextField()

	def __str__(self):
		return self.message