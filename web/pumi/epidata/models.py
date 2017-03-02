from django.db import models

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
