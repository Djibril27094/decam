from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.generics import  ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication , TokenAuthentication

from rest_framework import status
from .models import Commande,Client,Facture , Service , Category
from .serializers import CommandeSerializer,ClientSerializer,FactureSerializer, ServiceSerializer, CategorySerializer

from rest_framework.decorators import api_view , authentication_classes , permission_classes
# Commande
class CommandeListAPIView(ListAPIView):
    queryset = Commande.objects.order_by('-id')
    serializer_class = CommandeSerializer
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        qs= super().get_queryset()
        if "user_id" in self.kwargs:
            id_user = self.kwargs["user_id"]
            user = User.objects.filter(id=id_user).first()
            qs = Commande.objects.filter(user=user)
        return qs

class CommandeCreateAPIView(CreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

class CommandeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

    permission_classes = [IsAuthenticated]

# Client
class ClientListAPIView(ListAPIView):
    queryset = Client.objects.order_by('-id')
    serializer_class = ClientSerializer
    def get_queryset(self):
        qs = super().get_queryset()
        if "id_user" in self.kwargs:
            id_user = self.kwargs["id_user"]
            user = User.objects.filter(id=id_user).first()
            qs = Client.objects.filter(user=user)
        return qs
class ClientCreateAPIView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    

class ClientDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

# Service
class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.order_by('-id')
    serializer_class = ServiceSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class ServiceDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
# Facture
class FactureListAPIView(ListAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class FactureCreateAPIView(CreateAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class FactureDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

# Login
    
class LoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Both username and password are required'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({'error': 'Invalid username or password'},
                            status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        

        return Response({'token': token.key , 'status': "Succes","id_user": user.id})

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Déconnexion réussie.'}, status=status.HTTP_200_OK)
    
# dashboard
    
class CombinedView(APIView):

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     if "id_user" in self.kwargs:
    #         id_user = self.kwargs["id_user"]
    #         user = User.objects.filter(id=id_user).first()
    #         qs = Client.objects.filter(user=user)
    def get_queryset(self):
        qs = super().get_queryset()
        if "id_user" in self.kwargs:
            id_user = self.kwargs["id_user"]
            user = User.objects.filter(id=id_user).first()
            commande_count = Commande.objects.filter(user=user).count()
            client_count = Client.objects.filter(user=user).count()
            combined_data = {
                'commandes_count': commande_count,
                'clients_count': client_count,
            }

            response_data = {
                'counts': combined_data,
            }

            return Response(response_data)
        return qs


@api_view(['GET'])
@authentication_classes([BasicAuthentication , TokenAuthentication])
@permission_classes([IsAuthenticated])
def dashboard_count(request, user_id):

    commande_count = Commande.objects.filter(user=user_id).count()
    client_count = Client.objects.filter(user=user_id).count()
    service_count=Service.objects.count()
    category_count=Category.objects.count()
    combined_data = {
                'commandes_count': commande_count,
                'clients_count': client_count,
                'service_count': service_count,
                'category_count':category_count
            }

    response_data = {
        'counts': combined_data,
    }

    return JsonResponse(response_data)