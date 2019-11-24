from django.urls import path
from Role import views

app_name = 'Role'


urlpatterns = [
    path('index/', views.index, name='index'),
    path('addRole/', views.addRole, name='addRole'),
    path('edirRole/', views.edirRole, name='edirRole'),
]