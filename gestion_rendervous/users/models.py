from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('medecin', 'Médecin'),
        ('admin', 'Administrateur'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')
    
    # Using AbstractUser gives us: id, first_name (prenom), last_name (nom), email, password, etc.
    # We will enforce email uniqueness for login if needed, or stick to username.
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_role_display()})"

class PatientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role='patient')

class Patient(User):
    objects = PatientManager()

    class Meta:
        proxy = True
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        
    def consulter_evenements(self):
        # Implementation to get available slots
        pass
        
    def s_inscrire_evenement(self, evenement):
        pass

class MedecinManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role='medecin')

class Medecin(User):
    objects = MedecinManager()

    class Meta:
        proxy = True
        verbose_name = 'Médecin'
        verbose_name_plural = 'Médecins'
        
    def creer_evenement(self, **kwargs):
        # Generate new slot
        pass

class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role='admin')

class Admin(User):
    objects = AdminManager()

    class Meta:
        proxy = True
        verbose_name = 'Administrateur'
        verbose_name_plural = 'Administrateurs'
