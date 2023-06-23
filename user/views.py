from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.generic import *
from django.urls import reverse_lazy
from user.forms import (
    RegisterForm,
    UsersAuthenticationForm
)
from django.views.generic.edit import FormView

# register view
class ClientRegisterView(FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user:login')
    
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return super().form_invalid(form)


# login view
class UserLoginView(FormView):
    template_name = "account/login.html"
    form_class = UsersAuthenticationForm
    success_url = reverse_lazy('user:dashboard')
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return self.form_invalid(form)
    
    def form_invalid(self, form):
        return super(UserLoginView, self).form_invalid(form)
    


# dashboard view
class DashboardView(TemplateView):
    template_name = 'client/dashboard.html'
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user.user()
        return context
    

class AdminDashboardView(TemplateView):
    template_name = 'siteadmin/base.html'
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user.user()
        return context
    