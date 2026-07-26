from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    """
    Login View
    """

    if request.user.is_authenticated:
        return redirect("command_center")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("command_center")

        messages.error(request, "Invalid username or password.")
        return render(
            request,
            "login.html",
            {
                "error": "Invalid username or password."
            }
        )

    return render(request, "login.html")


def logout_view(request):
    """
    Logout View
    """

    logout(request)
    messages.success(request, "You have been logged out successfully.")

    return redirect("login")