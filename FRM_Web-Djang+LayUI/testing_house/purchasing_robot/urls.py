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
from . import views
from django.conf.urls import url

urlpatterns = [
    url('pruchasing_robot_base', views.pruchasing_robot_base, name='set_robot'),
    url('purchasing_robot_business_manager', views.pruchasing_robot_business, name='set_robot'),
    url('purchasing_robot_jobs_manager', views.pruchasing_robot_jobs, name='set_prokject'),
    url('purchasing_robot_create', views.pruchasing_robot_create, name='purchasing_robot_create'),
    url('purchase_robot_buession_info', views.set_purchase_robot_buession_info, name='set_purchase_robot_jobs_info'),
    url('purchase_robot_jobs_info', views.set_purchase_robot_jobs_info, name='set_purchase_robot_jobs_info'),
    url('purchase_delete_jobs_info', views.set_purchase_deletjobs_info, name='delete_jobs'),
    url('purchase_stop_jobs_info', views.set_purchase_stopjobs_info, name='stop_jobs'),
    url('purchase_start_jobs_info', views.set_purchase_startjobs_info, name = 'start_jobs'),

]
