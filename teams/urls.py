from django.urls import path

from teams import views

urlpatterns = [
    path('create/', views.CreateTeamPage.as_view(), name='create_team'),
    path('<int:id>/edit/', views.edit_team_details, name='edit_team_details'),
    path('<int:team_id>/', views.team_page, name='team_page')
]