from django.urls import path
from base import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.log_out, name="logOut"),
    path('signup/', views.signup, name="signup"),
    path('reset/<str:pk>/', views.reset, name="reset"),
    path('token', views.token, name="token"),
]
