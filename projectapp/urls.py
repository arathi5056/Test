from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('response/', views.home_view),
  path('thankyou/', views.responseform),
  #path('loaddata/', views.loaddata),
  path('',views.responseform),

 
]