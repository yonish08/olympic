from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import *
from user.models import Customer
from core.mixins import UserRequiredMixin, AdminRequiredMixin


# Create your views here.
# ADMIN SITE VIEW
# admin dashboard
class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/base.html'
    login_url = 'user:login'


class AdminAboutusView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/aboutus.html'
    login_url = 'user:login'


class AdminSportsView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/sports.html'
    login_url = 'user:login'


class AdminNewsView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/news.html'
    login_url = 'user:login'


class AdminCountryView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/country.html'
    login_url = 'user:login'


class AdminStandingView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/standing.html'
    login_url = 'user:login'


class AdminPlayerView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/player.html'
    login_url = 'user:login'


class AdminLiveView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/live.html'
    login_url = 'user:login'


class AdminHighlightView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/highlight.html'
    login_url = 'user:login'


class AdminFixturetView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/fixture.html'
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




    