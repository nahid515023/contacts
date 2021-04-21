
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add-contacts',views.addContacts,name='add-contacts'),
    path('profile',views.profile,name='profile'),
]
