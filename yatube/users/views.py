from django.contrib.auth.views import \
    PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, \
    LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import MyUserCreationForm


class MyUserCreationView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('posts:index')


class MyLoginView(LoginView):
    template_name = 'users/login.html'


class MyLogoutView(LogoutView):
    template_name = 'users/logged_out.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('users:password_change_done')


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class MyPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    success_url = reverse_lazy('users:password_reset_done')


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
