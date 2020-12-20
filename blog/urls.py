from django.urls import path 
from . import views


urlpatterns = [
    # path("",views.home),
    path("",views.home,name='home'),
    # path('about/',views.about),
    path('about/',views.about,name='about'),
    path('<int:id>/',views.detail,name='detail')

]
