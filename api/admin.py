from django.contrib import admin
from .models import Service,Category,Client,Facture , Commande , Employer
# Register your models here.
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Facture)
admin.site.register(Commande)
admin.site.register(Employer)

admin.site.site_header = 'Administration de DECAM'
admin.site.site_title = 'DECAM'