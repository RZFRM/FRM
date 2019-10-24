"""testing_house URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from  . import views
from django.conf.urls import url

urlpatterns = [
    url('pruchasing_robot_base', views.pruchasing_robot_base, name='pruchasing_robot_base'),
    url('purchasing_robot_business_manager', views.pruchasing_robot_business, name='pruchasing_robot_business'),
    url('purchasing_robot_jobs_manager', views.pruchasing_robot_jobs, name='pruchasing_robot_jobs'),

    url('purchasing_created', views.purchasing_created, name='purchasing_created'),

    url('purchaes_requisitions_create_data', views.purchaes_requisitions_create_data,
        name='purchaes_requisitions_create'),

    url('purchaes_requisitions_create', views.purchaes_requisitions_create, name='purchaes_requisitions_create'),
    url('purchaes_requisitions_determine', views.purchaes_requisitions_determine, name='purchaes_requisitions_determine'),
    url('purchaes_order_create', views.purchaes_order_create, name='purchaes_order_create'),
    url('purchaes_order_determine', views.purchaes_order_determine, name='purchaes_order_determine'),
    url('purchaes_storage_create', views.purchaes_storage_create, name='purchaes_storage_create'),
    url('purchaes_storage_determine', views.purchaes_storage_determine, name='purchaes_storage_determine'),
    url('purchaes_reimburse_create', views.purchaes_reimburse_create, name='purchaes_reimburse_create'),
    url('purchaes_reimburse_determine', views.purchaes_reimburse_determine, name='purchaes_reimburse_determine'),
    url('purchaes_payment_create', views.purchaes_payment_create, name ='purchaes_payment_create'),
    url('purchaes_payment_determine', views.purchaes_payment_determine, name ='purchaes_payment_determine'),
    url('purchaes_business_data_display', views.purchaes_business_data_display, name ='purchaes_business_data_display'),

    url('purchasing_created_data', views.purchasing_created_data, name='purchasing_created'),
    url('purchaes_order_create_data', views.purchaes_requisitions_create_data, name='purchaes_requisitions_create'),
    url('purchaes_storage_create_data', views.purchaes_requisitions_create_data, name='purchaes_requisitions_create'),
    url('purchaes_reimburse_create_data', views.purchaes_requisitions_create_data, name='purchaes_requisitions_create'),
    url('purchaes_payment_create_data', views.purchaes_requisitions_create_data, name='purchaes_requisitions_create'),


    url('pruchasing_robot_base', views.pruchasing_robot_base, name='set_robot'),
    url('purchasing_robot_business_manager', views.pruchasing_robot_business, name='set_robot'),
    url('purchasing_robot_jobs_manager', views.pruchasing_robot_jobs, name='set_prokject'),
    # url('purchasing_robot_create', views.pruchasing_robot_create, name='purchasing_robot_create'),
    url('purchase_robot_buession_info', views.set_purchase_robot_buession_info, name='set_purchase_robot_jobs_info'),
    url('purchase_robot_jobs_info', views.set_purchase_robot_jobs_info, name='set_purchase_robot_jobs_info'),
    url('create_purchase_number', views.set_create_purchase_number, name='set_purchase_robot_jobs_info'),
    # url('purchase_delete_jobs_info', views.set_purchase_deletjobs_info, name='delete_jobs'),
    # url('purchase_stop_jobs_info', views.set_purchase_stopjobs_info, name='stop_jobs'),
    # url('purchase_start_jobs_info', views.set_purchase_startjobs_info, name='start_jobs'),









]
