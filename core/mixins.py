from django.shortcuts import redirect
from django.views.generic import *
from user.models import Customer
from django.contrib.auth.mixins import AccessMixin

# admin mixins
class AdminRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        elif request.user.is_authenticated:
            return redirect('core:dashboard')
        else:
            return redirect('/')
        
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
        
    
# user mixins
class UserRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated and user.is_superuser:
            context['full_name'] = user.get_full_name()
            context['email'] = user.email
        else:
            customer = Customer.objects.get(user=user)
            context['full_name'] = customer.getFullName()
            context['email'] = customer.email
        return context