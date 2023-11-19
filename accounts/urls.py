from django.urls import path
from accounts.views import login, registro, editar_perfil, CambiarPassword, perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", login, name= "login"),
    path("logout/", LogoutView.as_view(template_name="accounts/logout.html"), name= "logout"),
    path("registro/", registro, name="register"),
    path("perfil/", perfil, name="perfil"),
    path("perfil/editar/", editar_perfil, name="editar_perfil"),
    path("perfil/editar/password/", CambiarPassword.as_view(), name="cambiar_password"),
]

