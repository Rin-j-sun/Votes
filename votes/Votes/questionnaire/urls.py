from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    #path('', ApplicationListView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', views.registration, name='registration'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('validate_username', validate_username, name='validate_username'),
    path('logout/', BBLogoutView.as_view(), name='logout'),
    #path('profil', ApplicationsByUserListView.as_view(), name='profil'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)