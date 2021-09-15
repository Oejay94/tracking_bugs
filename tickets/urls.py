from django.urls import path

from tickets import views

urlpatterns = [
    path('create/', views.CreateTicketPage.as_view(), name='create_ticket'),
    path('edit/', views.UpdateTicketPage.as_view(), name='update_ticket'),
    path('complete/', views.CompleteTicketPage.as_view(), name='complete_ticket'),
    path('<int:ticket_id>/', views.ticket_detail_page, name='ticket_detail')
]