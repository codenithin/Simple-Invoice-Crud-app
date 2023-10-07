from django.contrib import admin
from .models import InvoiceItem, Invoice



# Register your models here.
admin.site.register(Invoice)
admin.site.register(InvoiceItem)

