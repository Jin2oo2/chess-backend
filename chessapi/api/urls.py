from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("users/", views.UserListView.as_view(), name="users"),
    path("user/<int:pk>", views.UserRetrieveView().as_view(), name="user"),
    path(
        "user/<int:pk>/update/",
        views.UserRetrieveUpdateView().as_view(),
        name="update-user",
    ),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("games/", views.GameListView.as_view(), name="games"),
    path("newgame/", views.GameCreateView.as_view(), name="newgame"),
    path(
        "user/<int:user_id>/games", views.UserGamesListView.as_view(), name="user-games"
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
