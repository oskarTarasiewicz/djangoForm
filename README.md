# Aplikacja z zawodnikami piłki nożnej


### Testowane przy użyciu:

- django-admin: 4.1.5
- python: 3.10.10
- Windows 11

### Instrukcja obsługi

1. ``cd djangoForm``
2. ``py manage.py makemigrations users``
3. ``py manage.py migrate``
4. ``py manage.py runserver``
5. Wchodzimy na <a href="http://localhost:8000">http://localhost:8000</a> i dodajemy nowego zawodnika
6. Po poprawnym dodaniu zawodnika przekieruje nas na <a href="http://localhost:8000/users">http://localhost:8000/users </a>gdzie wyświetli z bazy danych obecnie wpisanych zawodników.
7. Po wejściu na <a href="http://localhost:8000/delete">http://localhost:8000/delete </a> pokaże nam się lista rozwijana z zawodnikami, których możemy usunąć z bazy, wybieramy jednego z listy i klikamy guzik **Usuń**


### Modele

```postcss
# model tabeli User
class User(models.Model):
  id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
  imie = models.CharField(max_length=30, null=True)
  nazwisko = models.CharField(max_length=50, null=True)
  telefon = models.IntegerField(null=True)
  dolaczenie = models.DateField(null=True)
  wiek = models.IntegerField(null=True)
```


### Endpointy

- insert_player - ``Endpoint odpowiadający za dodawanie zawodnika do bazy, przyjmuje body z requestu z formularza html``
- users - ``Strona z listą wpisanych zawodników oraz endpoint zwracający listę zawodników z bazy danych``
- delete - ``Strona z listą zawodników do usunięcia``
- delete_player - ``Endpoint odpowiadający za usuwanie zawodnika z bazy, przyjmuje body z requestu z formularza html``
- / - ``Strona główna z formularzem dodawania zawodnika``