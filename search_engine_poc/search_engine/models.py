from django.db import models

# Create your models here.
from django.db import models

class Application(models.Model):
    applicationNumber = models.CharField(max_length=100)
    applicationDate = models.DateField()
    registrationNumber = models.CharField(max_length=100)
    expiryDate = models.DateField()
    disclaimer = models.TextField(blank=True, null=True)
    colors = models.CharField(max_length=200, blank=True, null=True)
    markFeature = models.TextField(blank=True, null=True)
    verbalElements = models.TextField()  # Adjust max_length as per your needs
    comments = models.TextField(blank=True, null=True)
    validation_errors = models.TextField(blank=True, null=True)
    owners_name = models.CharField(max_length=200)
    owners_address = models.TextField()
    owners_country = models.CharField(max_length=100)
    representatives_name = models.CharField(max_length=200, blank=True, null=True)
    representatives_address = models.TextField(blank=True, null=True)
    representatives_country = models.CharField(max_length=100, blank=True, null=True)
    priorities_number = models.CharField(max_length=100, blank=True, null=True)
    priorities_date = models.DateField(blank=True, null=True)
    priorities_country = models.CharField(max_length=100, blank=True, null=True)
    publicationEvents_publicationNumber = models.CharField(max_length=100, blank=True, null=True)
    publicationEvents_publicationDate = models.DateField(blank=True, null=True)
    publicationEvents_sectionName = models.CharField(max_length=100, blank=True, null=True)
    publicationEvents_description = models.TextField(blank=True, null=True)
    publicationEvents_eventDetail = models.TextField(blank=True, null=True)
    classifications_niceClass = models.CharField(max_length=100, blank=True, null=True)
    classifications_localClass = models.CharField(max_length=100, blank=True, null=True)
    classifications_goodServiceDescription = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Application {self.applicationNumber}"
