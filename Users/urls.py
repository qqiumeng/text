from django.urls import path
from Users import views

app_name='Users'


urlpatterns = [
    path('index/', views.index.as_view(), name='index'),
    path('addUser/', views.addUser.as_view(), name='addUser'),
    path('editUser/<int:u_id>', views.editUser.as_view(), name='editUser'),
    path('password/', views.password.as_view(), name='password'),
    path('login/', views.login.as_view(), name='login'),
    path('drop/<int:u_id>', views.drop.as_view(), name='drop'),
    path('dropall/', views.dropall, name='dropall'),
    path('draw/', views.draw, name='draw'),
]