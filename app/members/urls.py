from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('login/', views.login_view, name='login-view'),
    path('logout/', views.logout_view, name='logout-view'),
    path('user_pick/', views.user_pick, name='user-pick'),
]