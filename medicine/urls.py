
from django.urls import path
from medicine import views

app_name = 'medicines'

urlpatterns = [
    path('index/', views.index.as_view(), name='index'),
    path('add/', views.add.as_view(), name='add'),
    path('update/<int:u_id>/',views.Update.as_view(),name='update'),
    path('add_medicine/<int:u_id>/', views.add_medicine.as_view(), name='add_medicine'),
    path('look/<int:u_id>/', views.look.as_view(), name='look'),
    path('dpro4/', views.dpro4, name='dpro4'),
    path('delete/<int:u_id>', views.delete, name='delete'),
]
