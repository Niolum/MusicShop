from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Customer)

admin.site.site_title = "MusicShop"
admin.site.site_header = "MusicShop"