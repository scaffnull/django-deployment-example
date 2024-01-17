from django.urls import path
from basic_app import views

# SETTING NAME SPACE TEMPLATE TAGGING!
# SET IT TO YOUR APP, THIS ALLOWS TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path("relative/", views.relative, name="relative"),
    path("other/", views.other, name="other"),
]
