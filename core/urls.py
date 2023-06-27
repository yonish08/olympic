from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('admin-about-us/', AdminAboutusView.as_view(), name='admin_about_us'),
    # sports CRUD
    path('admin-sports/', AdminSportsView.as_view(), name='admin_sports'),
    path('admin-sport-create', AdminSportsCreateView.as_view(), name='admin_sport_create'),
    path('admin-sport-update/<int:pk>/', AdminSportsUpdateView.as_view(), name='admin_sport_update'),
    path('admin-sport-delete/<int:pk>/', AdminSportsDeleteView.as_view(), name='admin_sport_delete'),
    # news CRUD
    path('admin-news/', AdminNewsView.as_view(), name='admin_news'),
    path('admin-news-create', AdminNewsCreateView.as_view(), name='admin_news_create'),
    path('admin-news-update/<int:pk>/', AdminNewsUpdateView.as_view(), name='admin_news_update'),
    path('admin-news-delete/<int:pk>/', AdminNewsDeleteView.as_view(), name='admin_news_delete'),
        # Country CRUD
    path('admin-country/', AdminCountryView.as_view(), name='admin_country'),
    path('admin-country-create', AdminCountryCreateView.as_view(), name='admin_country_create'),
    path('admin-country-update/<int:pk>/', AdminCountryUpdateView.as_view(), name='admin_country_update'),
    path('admin-country-delete/<int:pk>/', AdminCountryDeleteView.as_view(), name='admin_country_delete'),

    path('admin-standing/', AdminStandingView.as_view(), name='admin_standing'),
    # player CRUD
    path('admin-player/', AdminPlayerView.as_view(), name='admin_player'),
    path('admin-player-create', AdminPlayerCreateView.as_view(), name='admin_player_create'),
    path('admin-player-update/<int:pk>/', AdminPlayerUpdateView.as_view(), name='admin_player_update'),
    path('admin-player-delete/<int:pk>/', AdminPlayerDeleteView.as_view(), name='admin_player_delete'),
    path('admin-live/', AdminLiveView.as_view(), name='admin_live'),
    path('admin-highlight/', AdminHighlightView.as_view(), name='admin_highlight'),
    path('admin-fixture/', AdminFixturetView.as_view(), name='admin_fixture'),


    # client views
    path('', DashboardView.as_view(), name='dashboard'),
    path('about-us', AboutusView.as_view(), name='about_us'),
    path('fixture', FixtureView.as_view(), name='fixture'),
    path('highlight', HightlightView.as_view(), name='highlight'),
    path('live', LiveView.as_view(), name='live'),
    path('news', NewsView.as_view(), name='news'),
    path('news-detail', NewsDetailView.as_view(), name='news_detail'),
    path('player', PlayerView.as_view(), name='player'),
    path('sport', SportView.as_view(), name='sport'),
    # Search
    path('player-search/', playerSearchView, name='player_search'),
    path('sport-search/', sportSearchView, name='sport_search'),
]