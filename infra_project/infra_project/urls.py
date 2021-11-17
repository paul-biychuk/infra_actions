from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'infra_app'

urlpatterns = [
    path('', include('infra_app.urls', namespace='infra_app')),
    path('admin/', admin.site.urls),
    path('second_page/', views.second_page, name='second_page'),
]
