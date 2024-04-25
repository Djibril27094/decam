from django.db import models
from django.contrib.auth.models import User , AbstractUser 
# Create your models here.




class Employer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    addresse = models.CharField(max_length=100)
    profile=models.ImageField(upload_to="profile" , null=True)
    couverture=models.ImageField(upload_to="couverture" , null=True)

    class Meta:
        db_table='Employers'

    def __str__(self):
        return self.user.first_name
    
class Category(models.Model):
    libelle=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    
    class Meta:
        db_table='categories'

    def __str__(self):
        return self.libelle
    

class Client(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)
    telephone=models.CharField(max_length=255)
    addresse=models.CharField(max_length=100 , null=True)
    email=models.EmailField()
    created_at=models.DateTimeField(null=True)
    class Meta:
        db_table="clients"
    def __str__(self):
        return f"{self.nom}-{self.prenom}"


class Service(models.Model):
    category=models.ForeignKey(Category, verbose_name=("service"), on_delete=models.CASCADE)
    nom=models.CharField(max_length=255)
    description=models.TextField(null=True)
    prix_unitaire=models.FloatField()
    image=models.ImageField(upload_to="service" , null=True)

    class Meta:
        db_table='services'
    def __str__(self):
        return f"{self.nom}-{self.category.libelle}"
    


class Commande(models.Model):
    choix = (
    ('attente', 'En Attente'),
    ('termine', 'Terminé'),
    ('traitement', 'En traitement'),
  )
    user=models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    service=models.ForeignKey(Service , on_delete=models.CASCADE)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    quantite=models.IntegerField()
    prix_total=models.FloatField()
    date_depot=models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=choix, null=True)
    
    class Meta:
        db_table='Commandes'
    def __str__(self):
        return f" {self.service.nom}-{self.client.prenom}-{self.client.nom} "

class Facture(models.Model):
    reference=models.CharField(max_length=255)
    commande=models.ForeignKey(Commande,on_delete=models.CASCADE ,null=True)
    date=models.DateField(auto_now_add=True)
    
    class Meta:
        db_table="factures"
    
    def __str__(self):
        return f"{self.reference}"

    


    