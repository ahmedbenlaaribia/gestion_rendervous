from django.db import models
from users.models import Patient, Medecin

class Creneau(models.Model):
    # En UML c'est Evenement(id, titre, description, date, location, max-participants, statut, organisateur)
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_heure = models.DateTimeField()
    location = models.CharField(max_length=255)
    max_participants = models.PositiveIntegerField(default=1)
    
    STATUT_CHOICES = (
        ('disponible', 'Disponible'),
        ('complet', 'Complet'),
        ('annule', 'Annulé'),
        ('termine', 'Terminé'),
    )
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='disponible')
    
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, related_name='creneaux_crees') # organisateur
    
    def __str__(self):
        return f"{self.titre} le {self.date_heure.strftime('%Y-%m-%d %H:%M')}"

class RendezVous(models.Model):
    # En UML c'est Inscription(idinscription, dateinscription, statut, participant, evenement, organisateur)
    date_inscription = models.DateTimeField(auto_now_add=True)
    
    STATUT_CHOICES = (
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
        ('termine', 'Terminé'),
    )
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='confirme')
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='inscriptions') # participant
    creneau = models.ForeignKey(Creneau, on_delete=models.CASCADE, related_name='inscriptions') # evenement
    
    class Meta:
        unique_together = ('patient', 'creneau') # Un patient ne peut s'inscrire qu'une fois au même créneau
        verbose_name = 'Rendez-vous'
        verbose_name_plural = 'Rendez-vous'
        
    def __str__(self):
        return f"Rendez-vous pour {self.patient} au créneau {self.creneau.titre}"
