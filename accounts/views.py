from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, "signup.html", {"form": form})
