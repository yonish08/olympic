from django.urls import path
from .views import (
    AdminDashboardView,
    # client views
    DashboardView,
    AboutusView,
    FixtureView,
    HightlightView,
    LiveView,
    NewsView,
    NewsDetailView,
    PlayerView,
    SportView
)

app_name = 'core'

urlpatterns = [
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
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
]