from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.generic import *
from django.urls import reverse_lazy
from user.forms import UsersAuthenticationForm, RegisterForm
from user.models import Customer, SiteAdmin
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout

# register view
class ClientRegisterView(FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('core:admin-dashboard')
            else:
                return redirect('core:dashboard')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['email'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )
        user.is_active = False
        user.save()
        
        customer = Customer.objects.create(
            user=user,
            email=form.cleaned_data['email'],
            full_name=form.cleaned_data['full_name'],
            country=form.cleaned_data['country']
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return super().form_invalid(form)


# login view
class UserLoginView(FormView):
    template_name = "account/login.html"
    form_class = UsersAuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('core:admin-dashboard')
            else:
                return redirect('core:dashboard')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(username=email, password=password)
        if user is not None:
            login(self.request, user)
            if user.is_superuser:
                return redirect('core:admin-dashboard')  # Redirect to admin
            else:
                return redirect('core:dashboard')  # Redirect to client
        else:
            messages.error(self.request, "Invalid Email or Password")
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        return super(UserLoginView, self).form_invalid(form)
    
    
# Logout
class UserLogoutView(View):
    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.success(self.request, "Logged out successfully.")
            return redirect('/')