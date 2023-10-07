from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Invoice,InvoiceItem
from .forms import  InvoiceCreateForm, InvoiceItemCreateForm, InvoiceUpdateForm, InvoiceItemUpdateForm, InvoiceDetailForm, InvoiceItemDetailForm, InvoiceDeleteForm, InvoiceItemDeleteForm, InvoiceInlineFormSet

# Create your views here.
class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice/invoice_list.html'
    context_object_name = 'invoices'
    paginate_by = 10

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoice/invoice_detail.html'
    context_object_name = 'invoice'

class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceCreateForm
    template_name = 'invoice/invoice_create.html'
    
    success_url = '/'   
    """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
    """    
    def get_context_data(self, **kwargs):
        context = super(InvoiceCreateView, self).get_context_data(**kwargs)
        context['invoice_item_formset'] = InvoiceInlineFormSet()
        return context
    """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
    """    
    def post(self, request, *args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        invoice_item_formset = InvoiceInlineFormSet(self.request.POST)
        if form.is_valid() and invoice_item_formset.is_valid():
            return self.form_valid(form , invoice_item_formset)
        else:
            return self.form_invalid(form, invoice_item_formset)
    """
        Called if all forms are valid. Creates Invoice instance along with the
        associated Invoice Item instances then redirects to success url
        Args:
            form: Assignment Form
            assignment_question_form: Assignment Question Form

        Returns: an HttpResponse to success url

    """
    def form_valid(self, form, invoice_item_formset):
        self.object = form.save(commit=False)
        self.object.save()
        invoice_items = invoice_item_formset.save(commit=False)
        for invoice_item in invoice_items:
            invoice_item.invoice = self.object
            invoice_item.save()
        return redirect(reverse('invoice_list'))       
    """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.

        Args:
            form: Invoice Item Form
            invoice_item_formset: Invoice Item Formset
    """
    def form_invalid(self, form, invoice_item_formset):
        return self.render_to_response(
            self.get_context_data(form=form, invoice_item_formset=invoice_item_formset)
        )
        
class InvoiceUpdateView(UpdateView):
    model = Invoice
    template_name = 'invoice/invoice_update.html'
    success_url = '/'
    form_class = InvoiceDetailForm

    def get_object(self, queryset=None):
        self.object = super(InvoiceUpdateView, self).get_object()
        return self.object
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        invoice_item_formset = InvoiceInlineFormSet(instance=self.object)
        return self.render_to_response(
            self.get_context_data(form=self.get_form(), invoice_item_formset=invoice_item_formset)
        )
    
    def get_success_url(self):
        invoice = self.object.invoice
        return reverse('invoice_detail', kwargs={'pk': invoice.pk})
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        invoice_item_formset = InvoiceInlineFormSet(self.request.POST, instance=self.object)
        if form.is_valid() and invoice_item_formset.is_valid():
            return self.form_valid(form, invoice_item_formset)
        else:
            return self.form_invalid(form, invoice_item_formset)
    def form_valid(self, form, invoice_item_formset):
        self.object = form.save(commit=False)
        self.object.save()
        invoice_items = invoice_item_formset.save(commit=False)
        for invoice_item in invoice_items:
            invoice_item.invoice = self.object
            invoice_item.save()
        return redirect(reverse('invoice_list'))       

    def form_invalid(self, form, invoice_item_formset):
        return self.render_to_response(
            self.get_context_data(form=form, invoice_item_formset=invoice_item_formset)
        )
        
            


class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoice/invoice_delete.html'
    success_url = '/'

class InvoiceItemCreateView(CreateView):
    model = InvoiceItem
    template_name = 'invoice/invoiceitem_create.html'
    # form_class = InvoiceItemCreateForm
    fields = ['invoice','name','quantity','price']
    success_url = '/'


class InvoiceItemUpdateView(UpdateView):
    model = InvoiceItem
    template_name = 'invoice/invoiceitem_update.html'
    fields = ['name','quantity','price']
    success_url = '/'

class InvoiceItemDeleteView(DeleteView):
    model = InvoiceItem
    template_name = 'invoice/invoiceitem_delete.html'
    success_url = '/invoice/'

class InvoiceItemDetailView(DetailView):
    model = InvoiceItem
    template_name = 'invoice/invoiceitem_detail.html'
    context_object_name = 'invoiceitem'

class InvoiceItemListView(ListView):
    model = InvoiceItem
    template_name = 'invoice/invoiceitem_list.html'
    context_object_name = 'invoiceitems'
    paginate_by = 10


