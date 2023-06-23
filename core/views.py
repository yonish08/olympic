from django.shortcuts import render
from django.views.generic import *
from user.models import Customer

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'client/dashboard.html'
    login_url = 'core:dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        customer = Customer.objects.get(user=user)
        context['full_name'] = customer.getFullName()
        context['email']= customer.email
        return context
    

class AdminDashboardView(TemplateView):
    template_name = 'siteadmin/base.html'
    login_url = 'core:admin-dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context