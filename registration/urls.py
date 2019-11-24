from django.urls import path
from registration import views

app_name = 'registrations'


urlpatterns = [
    path('guahao/', views.guahao.as_view(), name='guahao'),
    path('guahaogenggai/', views.guahaogenggai.as_view(), name='guahaogenggai'),
    path('gaohaoxiangqing/<int:u_id>/', views.gaohaoxiangqing, name='gaohaoxiangqing'),
    path('guahaoedit/<int:p_id>/', views.guahaoedit.as_view(), name='guahaoedit'),
    path('export/',views.export,name = 'export'),
    path('exit/<int:k_id>',views.exit,name='exit'),
    path('exit2/',views.exit2,name='exit2'),
    path('get_doctor/',views.get_doctor,name='get_doctor'),

]
