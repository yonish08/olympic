from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import *
from user.models import Customer
from core.mixins import UserRequiredMixin, AdminRequiredMixin


# Create your views here.
# dashboard
class DashboardView(UserRequiredMixin, TemplateView):
    template_name = 'client/dashboard.html'
    login_url = 'user:login'


# admin dashboard
class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/base.html'
    login_url = 'user:login'




    