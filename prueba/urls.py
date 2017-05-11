from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^index', views.index, name='index'),
            url(r'pages/[sS]un[Bb]urst', views.SunBurst, name='sunburst'),
            url(r'pages/[hH]eat[mM]ap', views.heatmap, name='heatmap'),
            url(r'pages/[tT]axi[tT]racker', views.TaxiTracker, name='taxitracker'),
            url(r'pages/[gG]allery', views.TaxiTracker, name='taxitracker')
        ]
