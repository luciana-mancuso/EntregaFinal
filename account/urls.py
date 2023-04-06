
from django.urls import path, include
from account.views import *
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('login/', login_account, name="accountlogin"),
    path('registrar/', registrar_account, name="accountregistrar"),
    path('editar/', editar_usuario, name="accounteditar"),
    path('logout/', LogoutView.as_view(template_name="account/logout.html"), name="accountlogout"),
]
