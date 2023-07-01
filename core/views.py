from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import *
from core.mixins import UserRequiredMixin, AdminRequiredMixin
from user.models import Customer
from django.urls import reverse_lazy, reverse
from core.models import *
from core.forms import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage


# Create your views here.
# ADMIN SITE VIEW
# admin dashboard
class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/dashboard.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsCount'] = News.objects.count()
        context['countryCount'] = Country.objects.count()
        context['sportCount'] = Sport.objects.count()
        context['playerCount'] = Player.objects.count()
        context['highlightCount'] = Highlight.objects.count()
        context['liveCount'] = LiveMatch.objects.count()
        return context



# About us CRUD
class AdminAboutusView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/aboutus.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['org'] = AboutFunOlympic.objects.first()
        return context


class AdminAboutusCreateView(AdminRequiredMixin, CreateView):
    template_name  = 'siteadmin/aboutcreate.html'
    form_class = AboutFunOlympicForm
    success_url = reverse_lazy('core:admin_about_us')
    success_message = "About us created successfully!"

    def get_success_message(self, cleaned_data):
        title = cleaned_data['title']
        return title + self.success_message


class AboustUsUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "siteadmin/aboutupdate.html"
    model = AboutFunOlympic
    form_class = AboutFunOlympicForm
    success_url = reverse_lazy('core:admin_about_us')
    success_message = " updated successfully!"
    
    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_message(self, cleaned_data):
        title = cleaned_data['title']
        return title + self.success_message


class AboustUsDetail(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/aboutus.html'
    login_url = 'user:login'


# SPORTS CRUD
class AdminSportsView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/sport.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sportList = Sport.objects.all().order_by('-created_at')
        paginator      = Paginator(sportList, 12) 
        page_number    = self.request.GET.get('page')
        page_obj       = paginator.get_page(page_number)
        context['page_obj'] = page_obj
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newsList = News.objects.all().order_by('-created_at')
        paginator      = Paginator(newsList, 12) 
        page_number    = self.request.GET.get('page')
        page_obj       = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
    

class AdminNewsCreateView(AdminRequiredMixin, CreateView):
    template_name  = 'siteadmin/newscreate.html'
    form_class = NewsForm
    success_url = reverse_lazy('core:admin_news')
    success_message = "News created successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminNewsUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "siteadmin/newsupdate.html"
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('core:admin_news')
    success_message = "News updated successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminNewsDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "siteadmin/newsdelete.html"
    model = Sport
    success_url = reverse_lazy('core:admin_news')
    success_message = "News deleted successfully!"
    
    def form_valid(self, form):
        self.object = self.get_object()
        messages.success(self.request, self.object.title + ' ' + self.success_message)
        return super().form_valid(form)


# Country CRUD
class AdminCountryView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/country.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countryList = Country.objects.all().order_by('-created_at')
        paginator      = Paginator(countryList, 12) 
        page_number    = self.request.GET.get('page')
        page_obj       = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
    

class AdminCountryCreateView(AdminRequiredMixin, CreateView):
    template_name  = 'siteadmin/countrycreate.html'
    form_class = CountryForm
    success_url = reverse_lazy('core:admin_country')
    success_message = "Country created successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminCountryUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "siteadmin/countryupdate.html"
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('core:admin_country')
    success_message = "Country updated successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminCountryDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "siteadmin/countrydelete.html"
    model = Country
    success_url = reverse_lazy('core:admin_country')
    success_message = " country deleted successfully!"
    
    def form_valid(self, form):
        self.object = self.get_object()
        messages.success(self.request, self.object.country.name + ' ' + self.success_message)
        return super().form_valid(form)


# Standing CRUD
class AdminStandingView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/standing.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countryList = Standing.objects.all().order_by('-created_at')
        paginator      = Paginator(countryList, 10) 
        page_number    = self.request.GET.get('page')
        page_obj       = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
    

class AdminStandingCreateView(AdminRequiredMixin, CreateView):
    template_name  = 'siteadmin/standingcreate.html'
    form_class = StandingForm
    success_url = reverse_lazy('core:admin_standing')
    success_message = "Standing created successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminStandingUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "siteadmin/standingupdate.html"
    model = Standing
    form_class = StandingForm
    success_url = reverse_lazy('core:admin_standing')
    success_message = "Standing updated successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminStandingDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "siteadmin/standingdelete.html"
    model = Standing
    success_url = reverse_lazy('core:admin_standing')
    success_message = " standing deleted successfully!"
    
    def form_valid(self, form):
        self.object = self.get_object()
        messages.success(self.request, self.object.title + ' ' + self.success_message)
        return super().form_valid(form)


# Player CRUD
class AdminPlayerView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/player.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerList = Player.objects.all().order_by('-created_at')
        paginator      = Paginator(playerList, 12) 
        page_number    = self.request.GET.get('page')
        page_obj       = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
    

class AdminPlayerCreateView(AdminRequiredMixin, CreateView):
    template_name  = 'siteadmin/playercreate.html'
    form_class = PlayerForm
    success_url = reverse_lazy('core:admin_player')
    success_message = "Player added successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminPlayerUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "siteadmin/playerupdate.html"
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy('core:admin_player')
    success_message = "Player data updated successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminPlayerDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "siteadmin/playerdelete.html"
    model = Player
    success_url = reverse_lazy('core:admin_player')
    success_message = " player deleted successfully!"
    
    def form_valid(self, form):
        self.object = self.get_object()
        messages.success(self.request, self.object.name + ' ' + self.success_message)
        return super().form_valid(form)


# Live CRUD
class AdminLiveView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/live.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerList = LiveMatch.objects.all().order_by('-created_at')
        paginator      = Paginator(playerList, 12) 
        page_number    = self.request.GET.get('page')
        page_obj       = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
    

class AdminLiveCreateView(AdminRequiredMixin, CreateView):
    template_name  = 'siteadmin/livecreate.html'
    form_class = LiveMatchForm
    success_url = reverse_lazy('core:admin_live')
    success_message = "Live match added successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminLiveUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "siteadmin/liveupdate.html"
    model = LiveMatch
    form_class = LiveMatchForm
    success_url = reverse_lazy('core:admin_live')
    success_message = "Live match updated successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminLiveDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "siteadmin/livedelete.html"
    model = LiveMatch
    success_url = reverse_lazy('core:admin_live')
    success_message = "Live match deleted successfully!"
    
    def form_valid(self, form):
        self.object = self.get_object()
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


# Highlight live
class AdminHighlightView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/highlight.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerList = Highlight.objects.all().order_by('-created_at')
        paginator      = Paginator(playerList, 12) 
        page_number    = self.request.GET.get('page')
        page_obj       = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
    

class AdminHighlightCreateView(AdminRequiredMixin, CreateView):
    template_name  = 'siteadmin/highlightcreate.html'
    form_class = HighlightForm
    success_url = reverse_lazy('core:admin_highlight')
    success_message = "Match highlight added successfully!"

    def form_invalid(self, form):
        print("admin highlight create form is not valid.........")
        return super().form_invalid(form)
    
    def form_valid(self, form):
        print("admin highlight create form is valid.........")
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminHighlightUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "siteadmin/highlightupdate.html"
    model = Highlight
    form_class = HighlightForm
    success_url = reverse_lazy('core:admin_highlight')
    success_message = "Match highlight updated successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminHighlightDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "siteadmin/highlightdelete.html"
    model = Highlight
    success_url = reverse_lazy('core:admin_highlight')
    success_message = "Match highlight deleted successfully!"
    
    def form_valid(self, form):
        self.object = self.get_object()
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


# Fixture CRUD
class AdminFixturetView(AdminRequiredMixin, TemplateView):
    template_name = 'siteadmin/fixture.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerList = Fixture.objects.all().order_by('-created_at')
        paginator      = Paginator(playerList, 12) 
        page_number    = self.request.GET.get('page')
        page_obj       = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context


class AdminFixtureCreateView(AdminRequiredMixin, CreateView):
    template_name  = 'siteadmin/fixturecreate.html'
    form_class = FixtureForm
    success_url = reverse_lazy('core:admin_fixture')
    success_message = "Match fixture added successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminFixtureUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "siteadmin/fixtureupdate.html"
    model = Fixture
    form_class = FixtureForm
    success_url = reverse_lazy('core:admin_fixture')
    success_message = "Match fixture updated successfully!"

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.get_success_message()
        return response

    def get_success_message(self):
        messages.success(self.request, self.success_message)


class AdminFixtureDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "siteadmin/fixturedelete.html"
    model = Fixture
    success_url = reverse_lazy('core:admin_fixture')
    success_message = "Match fixture deleted successfully!"
    
    def form_valid(self, form):
        self.object = self.get_object()
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['player'] = Player.objects.all().order_by('-created_at')[0:36]
        return context
    
    
# search player
def playerSearchView(request):
    if request.method == 'GET':
        print("Player search")
        if request.GET['search']:        
            query =  request.GET.get('search')
            try:
                player_lookups = Q(name__icontains=query)
                player_filters = Player.objects.filter(player_lookups) 
                context = {
                    'playerFilter' : player_filters,
                } 
                return render(request,"client/playersearch.html",context)
            except:
                pass
            return render(request,"client/playersearch.html")
        else:
            return render(request,"client/playersearch.html")
    else:
        return render(request,"client/playersearch.html")


class SportView(UserRequiredMixin, TemplateView):
    template_name = 'client/sport.html'
    login_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sport'] = Sport.objects.all().order_by('-created_at')[0:21]
        return context
    

# search sport
def sportSearchView(request):
    if request.method == 'GET':
        if request.GET['search']:        
            query =  request.GET.get('search')
            try:
                program_lookups = Q(title__icontains=query)
                sport_filter = Sport.objects.filter(program_lookups) 
                context = {
                    'sportFilter' : sport_filter,
                } 
                return render(request,"client/sportsearch.html",context)
            except:
                pass
            return render(request,"client/sportsearch.html")
        else:
            return render(request,"client/sportsearch.html")
    else:
        return render(request,"client/sportsearch.html")




    