from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"


class Treaty(models.Model):
    country1 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country1_treaties')
    country2 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country2_treaties')
    pdf_url = models.URLField(blank=True, verbose_name="PDF URL")

    def __str__(self):
        return f"{self.country1.code}-{self.country2.code} Treaty"
    
    class Meta:
        verbose_name_plural = "Treaties"
        unique_together = ['country1', 'country2']
    