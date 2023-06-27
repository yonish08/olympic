from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import *
from core.mixins import UserRequiredMixin, AdminRequiredMixin
from user.models import Customer
from django.urls import reverse_lazy, reverse
from core.models import *
from core.forms import *


# Create your views here.
# ADMIN SITE VIEW
# admin dashboard
class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/base.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



# About us CRUD
class AdminAboutusView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/aboutus.html'
    login_url = 'user:login'


class AdminAboutusCreateView(AdminRequiredMixin, CreateView):
    template_name  = 'siteadmin/member_create.html'
    form_class = AboutFunOlympicForm
    success_url = reverse_lazy('core:admin_about_us')
    success_message = "About us created successfully!"

    def get_success_message(self, cleaned_data):
        title = cleaned_data['title']
        return title + self.success_message


class AboustUsUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "admintemplate/aboutus_update.html"
    model = AboutFunOlympic
    form_class = AboutFunOlympicForm
    success_url = reverse_lazy('core:admin_about_us')
    success_message = " updated successfully!"
    
    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_message(self, cleaned_data):
        title = cleaned_data['title']
        return title + self.success_message



# SPORTS CRUD
class AdminSportsView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/sport.html'
    login_url = 'user:login'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sport'] = Sport.objects.all()
        return context


class AdminSportsCreateView(AdminRequiredMixin, CreateView):
    template_name  = 'siteadmin/sportcreate.html'
    form_class = SportForm
    success_url = reverse_lazy('core:admin_sports')
    success_message = "Sport created successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminSportsUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "siteadmin/sportupdate.html"
    model = Sport
    form_class = SportForm
    success_url = reverse_lazy('core:admin_sports')
    success_message = "Sport updated successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)
    

class AdminSportsDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "siteadmin/sportdelete.html"
    model = Sport
    success_url = reverse_lazy('core:admin_sports')
    success_message = "Sport deleted successfully!"
    
    def form_valid(self, form):
        self.object = self.get_object()
        messages.success(self.request, self.object.title + ' ' + self.success_message)
        return super().form_valid(form)



# NEWS CRUD
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




    