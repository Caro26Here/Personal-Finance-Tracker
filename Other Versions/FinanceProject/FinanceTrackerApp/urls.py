from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('index', views.index, name='index'),
    path('signout', views.signout, name='signout'),
    path('goal', views.goal, name='goal'),
    path('settings', views.settings, name='settings'),
    path('')
    
]