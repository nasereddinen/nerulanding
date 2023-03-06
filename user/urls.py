from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from .views import (GDTLoginView, LogoutView, MyProgressView,
                    PasswordChangeDoneView, PasswordResetConfirmView,
                    PasswordResetDoneView, PasswordResetView,
                    PortalGoalsDetailView, SignUpView, delete_portal_goal, TermsView,
                    APIloginView)

app_name = 'user'
urlpatterns = [
    url(r'^login/$', GDTLoginView.as_view(), name='login'),
    url(r'^login_api/$', APIloginView.as_view(), name='login_api'),
    url('logout/', LogoutView.as_view(), name='logout'),
    url('signup/', SignUpView.as_view(), name='signup'),
    url('terms/', TermsView.as_view(), name='terms'),
    url(r'forgot-password/',
        PasswordResetView.as_view(email_template_name='email_templates''/reset_password_email.html'),
        name="password_change"),
    url(r'forgot-password-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    url(r'password-change-done/', PasswordChangeDoneView.as_view(), name="password_change_done"),
    path(r'forgot-passwordreset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    url('my-progress', login_required(MyProgressView.as_view(), login_url='/user/login'), name='myprogress'),
    path('delete_portal_goal/<slug:pk>/', delete_portal_goal, name='delete_portal_goal'),
    path('my-portal-goals/<slug:slug>/', PortalGoalsDetailView.as_view(), name="portal_goals"),
    url(r'my-portal-goals/[0-9A-Za-z_\-]+/', include('business.urls')),

]
