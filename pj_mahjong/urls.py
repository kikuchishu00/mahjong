"""pj_mahjong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from mahjong_stats import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('stats', views.StatsViewSet,'stats')

urlpatterns = [
    path('mahjong_admin/', admin.site.urls),
    path('', login_required(views.IndexView.as_view()), name="index"),
    path('', include(router.urls)),
    path('', include("django.contrib.auth.urls")),
    path('signup/',views.SignupView.as_view(),name="signup"),
    path('add/',views.DataAddView.as_view(),name='add'),
    path('top/',views.DataTopView.as_view(),name="top"),
    path('show/',views.DataShowView.as_view(),name="show"),
    path('update/<pk>',views.DataUpdateView.as_view(),name='update'),
    path('delete/<pk>', views.DataDeleteView.as_view(), name="delete"),
]
from django.conf.urls import url, static
import settings
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)