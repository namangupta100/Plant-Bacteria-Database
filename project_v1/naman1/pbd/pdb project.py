from django.db import models

class PlantProbioticBacteria(models.Model):
    genus = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    strain = models.CharField(max_length=100)
    plant_host = models.TextField()
    function = models.TextField()
    mode_of_action = models.TextField()
    reference = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.genus} {self.species} {self.strain}"

    class Meta:
        verbose_name_plural = "Plant Probiotic Bacteria"
