from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    # About fun olympic CRUD
    path('admin-about-us/', AdminAboutusView.as_view(), name='admin_about_us'),
    path('admin-about-create', AdminAboutusCreateView.as_view(), name='admin_about_create'),
    path('admin-about-update/<int:pk>/', AboustUsUpdateView.as_view(), name='admin_about_update'),
    path('admin-about-view/<int:pk>/', AboustUsDetail.as_view(), name='admin_about_view'),
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
    # standing CRUD
    path('admin-standing/', AdminStandingView.as_view(), name='admin_standing'),
    path('admin-standing-create', AdminStandingCreateView.as_view(), name='admin_standing_create'),
    path('admin-standing-update/<int:pk>/', AdminStandingUpdateView.as_view(), name='admin_standing_update'),
    path('admin-standing-delete/<int:pk>/', AdminStandingDeleteView.as_view(), name='admin_standing_delete'),
    # player CRUD
    path('admin-player/', AdminPlayerView.as_view(), name='admin_player'),
    path('admin-player-create', AdminPlayerCreateView.as_view(), name='admin_player_create'),
    path('admin-player-update/<int:pk>/', AdminPlayerUpdateView.as_view(), name='admin_player_update'),
    path('admin-player-delete/<int:pk>/', AdminPlayerDeleteView.as_view(), name='admin_player_delete'),
    # Live CRUD
    path('admin-live/', AdminLiveView.as_view(), name='admin_live'),
    path('admin-live-create', AdminLiveCreateView.as_view(), name='admin_live_create'),
    path('admin-live-update/<int:pk>/', AdminLiveUpdateView.as_view(), name='admin_live_update'),
    path('admin-live-delete/<int:pk>/', AdminLiveDeleteView.as_view(), name='admin_live_delete'),
    # Highlight CRUD
    path('admin-highlight/', AdminHighlightView.as_view(), name='admin_highlight'),
    path('admin-highlight-create', AdminHighlightCreateView.as_view(), name='admin_highlight_create'),
    path('admin-highlight-update/<int:pk>/', AdminHighlightUpdateView.as_view(), name='admin_highlight_update'),
    path('admin-highlight-delete/<int:pk>/', AdminHighlightDeleteView.as_view(), name='admin_highlight_delete'),
    # Fixture CRUD
    path('admin-fixture/', AdminFixturetView.as_view(), name='admin_fixture'),
    path('admin-fixture-create', AdminFixtureCreateView.as_view(), name='admin_fixture_create'),
    path('admin-fixture-update/<int:pk>/', AdminFixtureUpdateView.as_view(), name='admin_fixture_update'),
    path('admin-fixture-delete/<int:pk>/', AdminFixtureDeleteView.as_view(), name='admin_fixture_delete'),


    # client views
    path('', DashboardView.as_view(), name='dashboard'),
    path('about-us', AboutusView.as_view(), name='about_us'),
    path('fixture', FixtureView.as_view(), name='fixture'),
    path('highlight', HightlightView.as_view(), name='highlight'),
    path('live/<slug:slug>/', LiveView.as_view(), name='live'),
    path('live/<slug:slug>/comment/', LiveCommentView.as_view(), name='live_comment'),
    path('news', NewsView.as_view(), name='news'),
    path('news-detail/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('player', PlayerView.as_view(), name='player'),
    path('sport', SportView.as_view(), name='sport'),
    # Search
    path('player-search/', playerSearchView, name='player_search'),
    path('sport-search/', sportSearchView, name='sport_search'),
    path('news-search/', newsSearchView, name='news_search'),
        path('highlight-search/', highlightSearchView, name='highlight_search'),
]