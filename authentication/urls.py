from django.urls import path
from authentication.views import index, login_view, register_view, logout_view

urlpatterns = [
    path("", index, name="home"),
    path("signup", register_view, name="signup"),
    path("login", login_view, name="login"),
    path("logout_view", logout_view, name="logout"),
]
