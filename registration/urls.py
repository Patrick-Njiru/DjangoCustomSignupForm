from django.urls import path
from .views import login, signup

app_name = 'registration'
urlpatterns = [
    path('', login, name='login'),
    path('signup/', signup, name='signup')
]