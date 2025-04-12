from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, RegisterForm  # فرض می‌کنیم این فرم‌ها را داری

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "با موفقیت وارد شدید!")
                return redirect("home")  # یا هر صفحه‌ای که می‌خواهی
            else:
                messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form": form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "خروج موفقیت‌آمیز بود.")
    return redirect("login")

def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "ثبت‌نام انجام شد و وارد حساب شدید!")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {"form": form})
