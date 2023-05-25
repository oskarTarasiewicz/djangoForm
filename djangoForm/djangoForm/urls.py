from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('insert_player', include('users.urls')),
    path('delete', include('users.urls')),
    path('delete_player', include('users.urls')),
    path('/', include('users.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
]