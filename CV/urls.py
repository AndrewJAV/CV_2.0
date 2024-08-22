from django.contrib import admin
from django.urls import path
from cv_data import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showData, name='home'),
]
