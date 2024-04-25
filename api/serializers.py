from rest_framework import serializers
from .models import Service,Commande,Client,Facture, Category

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

    def __init__(self , *args , **kwargs):
        super(CommandeSerializer, self).__init__(*args , **kwargs)
        request = self.context.get("request")
        self.Meta.depth=0
        if request and request.method == "GET":
            self.Meta.depth=2

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

    def __init__(self , *args , **kwargs):
        super(ServiceSerializer, self).__init__(*args , **kwargs)
        request = self.context.get("request")
        self.Meta.depth=0
        if request and request.method == "GET":
            self.Meta.depth=2
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'
    
    def __init__(self , *args , **kwargs):
        super(FactureSerializer, self).__init__(*args , **kwargs)
        request = self.context.get("request")
        self.Meta.depth=0
        if request and request.method == "GET":
            self.Meta.depth=2