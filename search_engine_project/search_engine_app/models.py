from django.db import models

class PDFDocument(models.Model):
    applicationNumber = models.IntegerField()
    applicationDate = models.DateTimeField(max_length=200,blank=True,null=True)
    markFeature = models.CharField(max_length=200)
    registrationNumber = models.IntegerField(blank=True,null=True)
    expiryDate = models.DateTimeField(max_length=200,blank=True,null=True)
    disclaimer = models.TextField(blank=True,null=True)
    colors = models.CharField(max_length=200,blank=True,null=True)
    verbalElements = models.TextField(blank=True,null=True)
    owners_name = models.TextField(blank=True,null=True)
    owners_address = models.TextField(blank=True,null=True)
    owners_country = models.TextField(blank=True,null=True)
    representatives_name = models.TextField(blank=True,null=True)
    representatives_address = models.TextField(blank=True,null=True)
    representatives_country = models.TextField(blank=True,null=True)
    classifications_niceClass = models.TextField(blank=True,null=True)
    classifications_goodServiceDescription = models.TextField(blank=True,null=True)

    
    
    class Meta:
        managed = True
        db_table = 'corsearch_data'