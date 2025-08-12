from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("issue", views.issue, name="issue"),
    path("login/", include([
        path("", views.login, name="login"),
        path("register/", views.register, name="register"),
    ])),
    path("logout", views.logout, name="logout"),
    path("return_item", views.return_item, name="return_item"),
    path("history", views.history, name="history"),
]