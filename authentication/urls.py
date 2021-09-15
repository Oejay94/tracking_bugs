from django.urls import path

from authentication import views

urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login_page'),
    path('create/', views.CreateAccountPage.as_view(), name='create_account'),
    path('logout/', views.logout_button, name='logout')
]