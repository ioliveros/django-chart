from django.urls import path, include
from charts.views import ChartsView

urlpatterns = [
    path('plot', ChartsView.as_view()),
]