from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.ProfileCreate.as_view(), name="create"),
    path('update/', views.ProfileUpdate.as_view(), name="update"),
    path('login/',  views.ProfileLogin.as_view(), name="login"),
    path('logout/',  views.ProfileLogout.as_view(), name="logout")
]

