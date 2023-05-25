from django.db import models

class User(models.Model):
  id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
  imie = models.CharField(max_length=30, null=True)
  nazwisko = models.CharField(max_length=50, null=True)
  telefon = models.IntegerField(null=True)
  dolaczenie = models.DateField(null=True)
  wiek = models.IntegerField(null=True)