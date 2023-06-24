from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import *
from user.models import Customer
from core.mixins import UserRequiredMixin, AdminRequiredMixin


# Create your views here.

# admin dashboard
class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/base.html'
    login_url = 'user:login'



# CLIENT SITE VIEW
# dashboard
class DashboardView(UserRequiredMixin, TemplateView):
    template_name = 'client/dashboard.html'
    login_url = 'user:login'


class AboutusView(UserRequiredMixin, TemplateView):
    template_name = 'client/aboutus.html'
    login_url = 'user:login'


class FixtureView(UserRequiredMixin, TemplateView):
    template_name = 'client/fixtures.html'
    login_url = 'user:login'


class HightlightView(UserRequiredMixin, TemplateView):
    template_name = 'client/highlight.html'
    login_url = 'user:login'


class LiveView(UserRequiredMixin, TemplateView):
    template_name = 'client/live.html'
    login_url = 'user:login'


class NewsView(UserRequiredMixin, TemplateView):
    template_name = 'client/news.html'
    login_url = 'user:login'


class NewsDetailView(UserRequiredMixin, TemplateView):
    template_name = 'client/newsdetail.html'
    login_url = 'user:login'


class PlayerView(UserRequiredMixin, TemplateView):
    template_name = 'client/player.html'
    login_url = 'user:login'


class SportView(UserRequiredMixin, TemplateView):
    template_name = 'client/sport.html'
    login_url = 'user:login'




    