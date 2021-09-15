from django.urls import path

from projects import views

urlpatterns = [
    path('create/', views.ProjectFormPage.as_view(), name='create_project'),
    path('<int:id>/edit/', views.edit_project_details, name='edit_project_details'),
    path('<int:id>/', views.project_page, name='project_page')
]