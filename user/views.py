from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.generic import *
from django.urls import reverse_lazy
from user.forms import UsersAuthenticationForm, RegisterForm
from user.models import Customer
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout
# send meail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token

# activate account
class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Customer.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, Customer.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.is_active = True
            user.active = True
            user.save()
            messages.success(request, "Thank you for your email confirmation. Now you can login to your account.")
        else:
            messages.error(request, "Activation link is invalid!")
        return redirect(reverse_lazy('user:login'))
    
    
# send mail
def sendMail(request, user, to_email):
    print("************************************************************")
    print("USER ", user)
    print("USER OK ", user.pk)
    print("To mail ", to_email)
    print("USER full name  ", user.full_name)
    print("************************************************************")
    mail_subject = "Activate your user account."
    message = render_to_string("account/acc_active_email.html", {
        'user': user.full_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user.full_name}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


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
        sendMail(self.request, customer, form.cleaned_data.get('email'))

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