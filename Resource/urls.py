from django.urls import path
from Resource import views

app_name='Resource'


urlpatterns = [
    path('index/', views.index.as_view(), name='index'),
    path('add/', views.add.as_view(), name='add'),
    path('edit/<int:u_id>', views.edit.as_view(), name='edit'),
    path('drop/<int:u_id>', views.drop.as_view(), name='drop'),
    path('dropall/', views.dropall, name='dropall'),
]