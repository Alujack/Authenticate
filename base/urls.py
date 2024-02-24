from django.contrib.urls import path

urlpatterns=[
    path('', views.login, name = "login")
     path('logout/', views.login, name = "logout")
    path('signup/', views.signup, name = "signup") 
    path('reset/<str:pk>/', views.reset, name = "reset") 
    path('token', views.token, name = "token")
]