"""main URL Configuration
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('charts/', include('charts.urls'))
]