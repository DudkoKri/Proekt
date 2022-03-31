from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='glav'),
    path('kamni', views.about, name='kamni'),
    path('reg', views.reg, name='reg'),
    path('vhod', views.vhod, name='vhod'),
    path('malahit',views.malahit),
    path('avant',views.avant),
    path('yant', views.yant),
    path('agat', views.agat),
    path('bir', views.bir),
]