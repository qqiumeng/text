from django.urls import path
from hospital import views

app_name='hospital'

urlpatterns = [
    path('', views.index, name='index'),
    path('index1/', views.index1, name='index1'),
    path('edit/<int:h_id>', views.edit, name='edit'),
    path('look/<int:h_id>', views.look, name='look'),
    path('account/', views.account, name='account'),
    path('account_look/<int:h_id>/', views.account_look, name='account_look'),
    path('account_look2/<int:h_id>/', views.account_look2, name='account_look2'),
    path('add/', views.add, name='add'),
    path('dpro/', views.dpro, name='dpro'),
    path('dpro2/', views.dpro2, name='dpro2'),
    path('dpro3/', views.dpro3, name='dpro3'),
    path('add_many/<int:h_id>', views.add_many, name='add_many'),
    path('charge/', views.charge, name='charge'),
    path('charge_2/', views.charge_2, name='charge_2'),
    path('charge_edit1/<int:c_id>/', views.charge_edit1, name='charge_edit1'),
    path('charge_new/<int:h_id>/', views.charge_new, name='charge_new'),
    path('dispensing/', views.dispensing, name='dispensing'),
    path('dispensing_give/<int:h_id>/', views.dispensing_give, name='dispensing_give'),
    path('dispensing_gives/', views.dispensing_gives, name='dispensing_gives'),
    path('dispensing_look/<int:h_id>/', views.dispensing_look, name='dispensing_look'),
    path('out_hospital/', views.out_hospital, name='out_hospital'),
    path('edit_status/', views.edit_status, name='edit_status'),
    path('dispend_all/', views.dispend_all, name='dispend_all'),
    path('delete/<int:c_id>/', views.delete, name='delete'),
    path('charge_edit2/', views.charge_edit2, name='charge_edit2'),
    path('show_info/', views.show_info, name='show_info'),
    path('add_dis/', views.add_dis, name='add_dis'),
]