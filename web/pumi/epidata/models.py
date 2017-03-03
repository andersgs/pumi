from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class AccountManager(BaseUserManager):
    def create_user(self, username, password, first_name, last_name):
        account = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, username, password, first_name, last_name):
        account = self.create_user(username, password, first_name, last_name)
        account = is_admin = True
        account = save()
        return account

    # def get_by_natural_key(self, username_):
    #     return self.get(code_number=username_)

class Account(AbstractBaseUser):
    '''
    A class to hold account information
    '''
    username = models.CharField(max_length=8, unique=True)

    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=30, blank=False)

    is_admin = models.BooleanField(default = False)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username

    def get_name(self):
        return self.first_name

class Epidata(models.Model):
    patient_firstname = models.CharField(max_length=50, blank=False)
    patient_surname = models.CharField(max_length=75, blank=False)
    patient_identifier = models.CharField(max_length=20, blank=False)
    patient_DOB = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, blank=False)
    creator_institution = models.CharField(max_length=50, blank=False)
    creator_division = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.patient_identifier
