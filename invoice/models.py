from django.db import models
import secrets
from .utils import custom_id
from datetime import timedelta, date
from djmoney.models.fields import MoneyField
from address.models import AddressField



# Create your models here.
class Invoice(models.Model):
  class Terms(models.IntegerChoices):
    Net1Day = 1
    Net7Day = 7
    Net14Day = 14
    Net30Day = 30
  
  class Status(models.TextChoices):
    Draft = "Dr"
    Pending = "Pe"
    Paid = "Pd"

 

  createdAt = models.DateField(auto_now_add=True)
  paymentDue= models.DateField(default=date.today)
  description = models.CharField(max_length=30)
  paymentTerms = models.IntegerField(choices=Terms.choices)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  phone = models.CharField(max_length=30)
  email = models.EmailField(max_length=254, default= "test@EmailField")
  status = models.CharField(max_length=10,choices=Status.choices)
  senderAddress = AddressField(related_name='SenderAddress', blank=True, null=True)
  clientAddress = AddressField(related_name='ClientAddress', blank=True, null=True)



  class Meta:
    ordering = ['createdAt']
    indexes = [models.Index(fields=['createdAt']),]

  def get_absolute_url(self):
    return "list"

class InvoiceItem(models.Model):
  invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
  name = models.CharField(max_length=30)
  quantity = models.IntegerField()
  price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
  total = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

  def __str__(self) -> str:
    return str(self.id)
  
  def get_cost(self):
    return self.price * self.quantity

  class Meta:
    ordering = ['invoice']
    indexes = [models.Index(fields=['invoice']),]
