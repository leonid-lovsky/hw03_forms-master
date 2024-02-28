from django.urls import path

from .views import MyUserCreationView, \
    MyPasswordChangeView, MyPasswordChangeDoneView, \
    MyPasswordResetView, MyPasswordResetDoneView, \
    MyPasswordResetConfirmView, MyPasswordResetCompleteView, \
    MyLoginView, MyLogoutView

app_name = 'users'

urlpatterns = [
    path('signup/', MyUserCreationView.as_view(), name='signup'),

    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),

    path('password_change/', MyPasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/', MyPasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('password_reset/', MyPasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', MyPasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', MyPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
