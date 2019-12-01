from django.db import models
from django.contrib.auth.models import AbstractUser
import json
from django.core import serializers


# class User(models.Model):
#    name = models.CharField(max_length=100, null=False, default='self')
#    nick = models.CharField(max_length=100, null=True, unique=True)
#    avatar = models.URLField()
# Create your models here.

class User(AbstractUser):
    avatar = models.URLField(null=True, default='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAdVBMVEUAAAD///+Wlpby8vK2trbHx8dra2shISHDw8PZ2dk8PDy8vLzT09MMDAz19fWmpqacnJxEREQVFRVZWVmkpKQxMTHg4OA3Nzfr6+t5eXmwsLCIiIiAgICSkpJwcHCMjIwnJydgYGDOzs5NTU0aGhosLCxBQUFaNny0AAADfklEQVR4nO3a6XqiMBiGYVBgtCiLWxVXqtPzP8QpKpYvBNQZCHau5/5JSJpXQkiglgUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOrFmygMo0081pQdvF6YzLbe/IF2JvFuH4VJGO29z0nTnXzU7mOUc07nI7HTt68CdyfPPvQWeZm99Kd1DU885/vczCLxukg5LfbBzY4ktuyX933yKQxk4agy43vSt8v64Xv7kRQ90YGJdVyWuuXk5640nQ71zSblM68SU8lyMqG10nVqdDl1oO3xSNNoGmhPvQhSowGVhDN9p7IU84W+zP4otRnV5Mv0uktYybFi3W11ESlNhnebqxjaXSa099UBbTt+ukWTV/HBhLUGxQbTh6rUPmcMJAxqZ4pyYeERMFEuduBvd96q5yqVgi4T9ntZh6f6mdPNJsK3SOlvYdDJmzBY58fHyvSj3rwGEzr5umNfzhfkT39l3hnempuI48vi8z2VTekWhEYSFi6HowYsdFh2165o7k38KfmsXVuGKAmLg2euBOyfCoUjUXSbTcWKSF2+iDpDyxCZ0BdlHzKhWFLKC7K5Ho3FUXX3IeuYWqGKhMGhusyWuwx5w+WXfls8uFD/1jyobq89ctX2S5R5db+5KMvHo5iA5YDIiDFsamFTl1DsrNSHtOitrztYXriIG7G8nm1HXUJ5V3myoliIX1c1EzEMh77CET9AaRB3kPCtLuFQk1BWuGNpaMPfaMLjMwmVP/YzEsob947g/094IOELJnzqPvyRo/SpudSxzGg0ofI8dOp0s7f414RyTWPqIt3RbEK3eFD3JrUDzSaUOxVj2/hazSY81tW4GJ+1EaVCswkt8f6mvI1Pb7XcduJoNJxQvlHbyCriRdy2rUSqhhOeRBV7JaqIryLGvkE1nFD9rDY43kqOYqK1Z63GKmg64Un9wLEczPbrfeSr3yXVEdyaphMqL3eq/TYQ7qzxhHe/Hl782Lk0c//74RdDGwurlYSPXEXtYqAdbSSs/47/JTD4+VC+pe7L11/vf5vwzkhNjC5YxUpS7Wjxnaj60kH8NCtLNZ+V/23lbBE98s9UTUoHbm6m/ran5Fbmx2rF9a3M1T/bprOhfDj2h/7ms40MHRofpqv1trfdb3bp5+k1dlMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALyiPxkDKsG65uWEAAAAAElFTkSuQmCC')
    password = models.CharField(max_length=100, null=False, default='qwerty')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def to_json(self):
        return json.dumps({'avatar': self.avatar, 'date_joined': str(self.date_joined), 'email': self.email,
                           'is_active': self.is_active, 'is_staff': self.is_staff, 'is_superuser': self.is_superuser,
                           'last_login': self.last_login, 'username': self.username,
                           'first_name': self.first_name, 'last_name': self.last_name}, ensure_ascii=False)

    class Meta:
        verbose_name = "Пользователь",
        verbose_name_plural = "Пользователи"
