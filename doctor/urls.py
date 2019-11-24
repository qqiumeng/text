from django.urls import path
from doctor import views

app_name='doctor'

urlpatterns = [
    path('index/',  views.index.as_view(), name='index'),
    path('add/',  views.add.as_view(), name='add'),
    path('look/<int:e_id>/', views.look.as_view(), name='look'),
    path('edit/<int:e_id>/', views.edit.as_view(), name='edit'),
    path('dpro/',views.dpro,name='dpro'),
    path('check_verify/',views.check_verify,name='check_verify'),
    path('delete/<int:e_id>',views.delete,name='delete'),
]