from .views import Bugs_in
from django.urls import path

urlpatterns = [
        path('reportbugs/',Bugs_in,name='Bug_in')
]