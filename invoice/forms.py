from django import forms
from .models import Invoice, InvoiceItem
from django.forms import inlineformset_factory  

class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        prefix = 'header'
        fields = ['paymentDue','description','paymentTerms','status','senderAddress','clientAddress']

class InvoiceItemCreateForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        prefix = 'item'
        fields = ['invoice','name','quantity','price','total']

class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['paymentDue','description','paymentTerms','status','senderAddress','clientAddress']

class InvoiceItemUpdateForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['name','quantity','price','total']

class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['paymentDue','description','paymentTerms','status','senderAddress','clientAddress']

class InvoiceItemDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['invoice','name','quantity','price','total']
    
class InvoiceDeleteForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = []

class InvoiceItemDeleteForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = []

InvoiceInlineFormSet = forms.inlineformset_factory(
    Invoice, InvoiceItem, form=InvoiceItemCreateForm, extra=3, can_delete=True
)