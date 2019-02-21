from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products' , views.products , name = 'products'),
    path('programs' , views.all_programs , name = 'programs'),
    path('programs/slim' , views.slim_programs , name = "slim_programs"),
    path('programs/detox' , views.detox_programs , name = "detox_programs"),
    path('whygetfit', views.why_getfit, name="why_getfit"),
]