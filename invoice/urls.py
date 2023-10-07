from django.urls import path

from . import views

urlpatterns = [
    path('', views.InvoiceListView.as_view(), name='invoice_list'),
    path('invoice/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice_detail'),
    path('invoice/create/', views.InvoiceCreateView.as_view(), name='invoice_create'),
    path('invoice/<int:pk>/update/', views.InvoiceUpdateView.as_view(), name='invoice_update'),
    path('invoice/<int:pk>/delete/', views.InvoiceDeleteView.as_view(), name='invoice_delete'),
    path('invoiceitem/', views.InvoiceItemListView.as_view(), name='invoiceitem_list'),
    path('invoiceitem/<int:pk>/', views.InvoiceItemDetailView.as_view(), name='invoiceitem_detail'),
    path('invoiceitem/create/', views.InvoiceItemCreateView.as_view(), name='invoiceitem_create'),
    path('invoiceitem/<int:pk>/update/', views.InvoiceItemUpdateView.as_view(), name='invoiceitem_update'),
    path('invoiceitem/<int:pk>/delete/', views.InvoiceItemDeleteView.as_view(), name='invoiceitem_delete'),
]