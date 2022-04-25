from django.contrib import admin
from .models import ShippedProduct, YourMessage

admin.site.site_header = "            "

class ShippedProductAdmin(admin.ModelAdmin):
	list_display = ("tracking_id", "payment_status", "product_status", "product_name", "shipment_product_details", "receivers_full_name")
	list_filter = ("receivers_full_name", )
	search_fields = ("receivers_full_name", )
	filter_horizontal = ()
	fieldsets = ()

admin.site.register(ShippedProduct, ShippedProductAdmin)


class YourMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'subject', 'message')
	list_filter = ('name', 'subject')
	search_fields = ('name', )
	filter_horizontal = ()
	fieldsets = ()

	class Meta:
		model = YourMessage


admin.site.register(YourMessage, YourMessageAdmin)
