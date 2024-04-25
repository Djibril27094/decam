from django.urls import path 
from .views import CombinedView, CommandeListAPIView,CommandeCreateAPIView,CommandeDetailAPIView, dashboard_count
from .views import ClientListAPIView,ClientCreateAPIView,ClientDetailAPIView
from .views import FactureListAPIView,FactureCreateAPIView,FactureDetailAPIView,ServiceListAPIView , CategoryListAPIView
from .views import LoginView , LogoutView

from rest_framework.authtoken import views

urlpatterns = [
    # Authentification 
    path('api-token-auth/', views.obtain_auth_token),
    path("auth-login/", LoginView.as_view()),
    path("auth-logout/", LogoutView.as_view()),
    #Commande
    path("commande-list/<int:user_id>",CommandeListAPIView.as_view()),
    path("commande-create/",CommandeCreateAPIView.as_view()),
    path("commande-detail/",CommandeDetailAPIView.as_view()),
    # Service
    path("service-list/",ServiceListAPIView.as_view()),
    path("category-list/",CategoryListAPIView.as_view()),
    #Client
    path("client-list/<int:user_id>",ClientListAPIView.as_view()),
    path("client-create/",ClientCreateAPIView.as_view()),
    path("client-detail/",ClientDetailAPIView.as_view()),
    # Employer
    # path("employer-list/", EmployerListAPIView.as_view()),
    # path("employer-create/", EmployerCreateAPIView.as_view()),
    # path("employer-detail/", EmployerDetailAPIView.as_view()),
    # Dashboard 
    path("dashboard-list/<int:user_id>", dashboard_count,name="dashboard"),
    #Facture
    path("facture-list/", FactureListAPIView.as_view()),
    path("facture-create/", FactureCreateAPIView.as_view()),
    path("facture-detail/", FactureDetailAPIView.as_view()),
]
