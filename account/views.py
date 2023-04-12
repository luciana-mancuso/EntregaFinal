from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from account.forms import UserRegisterForm
from account.models import Avatar

# Create your views here.

def login_account(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            user = authenticate(username=informacion['username'], password=informacion['password'])

            if user:
                login(request, user)
                return redirect("AppCoderDestinos")
            else:
                return redirect("AppCoderMuseos")

    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "account/login.html", context=context)


def registrar_account(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("accountlogin")

    form = UserRegisterForm()
    context = {"form": form}
    return render(request, "account/registrar_usuario.html", context=context)


def editar_usuario(request):
    user = request.user

    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            informacion = form.cleaned_data
            user.username = informacion["username"]
            user.email = informacion["email"]
            user.is_staff = informacion["is_staff"]

            try:
                user.avatar.imagen = informacion["imagen"]
            except:
                avatar = Avatar(user=user, imagen=informacion["imagen"])
                avatar.save()

            user.save()
            return redirect("accountlogin")

    form = UserRegisterForm(initial={"username": user.username, "email": user.email, "is_staff": user.is_staff})
    contex = {"form": form}
    return render(request, "account/editar_usuario.html", context=contex)
