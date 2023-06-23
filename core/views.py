from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import *
from user.models import Customer
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin


# Create your views here.
class AdminRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        elif request.user.is_authenticated:
            return redirect('core:dashboard')
        else:
            return redirect('/')
        
    

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'client/dashboard.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if self.request.user.is_authenticated and self.request.user.is_superuser:
            context['full_name'] = user.get_full_name()
            context['email'] = user.email
        else:
            customer = Customer.objects.get(user=user)
            context['full_name'] = customer.getFullName()
            context['email']= customer.email
        return context


class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/base.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if self.request.user.is_authenticated and self.request.user.is_superuser:
            context['full_name'] = user.get_full_name()
            context['email'] = user.email
        else:
            customer = Customer.objects.get(user=user)
            context['full_name'] = customer.getFullName()
            context['email']= customer.email
        return context


    