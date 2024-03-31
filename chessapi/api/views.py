from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, GameSerializer
from .models import User, Game
from rest_framework_simplejwt.tokens import RefreshToken


# List all the users only for admins
class UserListView(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Retrieve an user
class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"


# Update avatar image
class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    def partial_update(self, request, *args, **kwargs):
        user = self.user
        new_avatar = request.data.get("avatar")
        if new_avatar in None:
            return Response({"detail": "Valid avatar was not provided"}, status=400)
        user.avatar = new_avatar
        user.save()
        user_serializer = self.get_serializer(user)
        return Response(user_serializer.data, status=200)


# Sign Up API with username and password
class SignUpView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"detail": "Username and password are required."}, status=400
            )
        if User.objects.filter(username=username).exists():
            return Response(
                {"detail": "Username already exists. Choose a different one."},
                status=400,
            )

        user = User.objects.create_user(username=username, password=password)
        user_serializer = self.get_serializer(user)
        return Response(user_serializer.data, status=201)


# Login API with username and password
class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            user_serializer = self.get_serializer(user)
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "jwt_token": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                    "user": user_serializer.data,
                },
                status=200,
            )
        else:
            return Response({"detail": "Invalid credentials."}, status=400)


# Logout API for logged in users
class LogoutView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def post(self, request):
        logout(request)
        return Response({"detail": "Logout successful."})


# List all the games played
class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


# Craete game for logged in users
class GameCreateView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = GameSerializer

    def post(self, request, *args, **kwargs):
        player = request.user
        result = request.data.get("result")
        level = request.data.get("level")

        if not result or not level:
            return Response({"detail": "result is not provided"})
        game = Game.objects.create(player=player, result=result, level=level)
        game_serialzer = self.get_serializer(game)
        return Response(game_serialzer.data, status=201)


#  List games for specific a user
class UserGamesListView(generics.ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Game.objects.filter(player=user_id)
