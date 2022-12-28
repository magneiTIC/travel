from django.db import models

class Trajet (models.Model):
   depart=models.CharField(max_length=200)
   arrive=models.CharField(max_length=200)
   def __str__(self):
       return self.depart + '-'+ self.arrive
   pass 

class Compagnie (models.Model):
    nom=models.CharField(max_length=200)
    logo=models.ImageField(upload_to='static/logoFiles')
    def __str__(self):
       return self.nom
    pass
    
class Vol (models.Model):
    prix=models.FloatField()
    date=models.CharField(max_length=200)
    heure=models.CharField(max_length=200)
    trajet=models.ForeignKey(Trajet,on_delete=models.CASCADE)
    compagnies=models.ManyToManyField(Compagnie)
    def __str__(self):
       return str(self.prix) + ' '+ self.date + ' '+ self.heure

#compagnie.vol_set
#vol.compagnies