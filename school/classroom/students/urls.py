from django.urls import path
from . import views
urlpatterns = [
    path('',views.register,name='register'),
    path('viewregister',views.viewregister,name='viewregister'),
    path('namesearch',views.namesearch,name='namesearch'),
    path('findname',views.findname,name='findname',)
]
