from django.shortcuts import render
from django.http import JsonResponse
from .models import PDFDocument



def import_site(request):
    if request.method == 'GET':
        searchText = request.GET.get('searchText', '')
        searchField = request.GET.get('searchField', '')
        if searchField and searchText:
            pdf_instance = PDFDocument.objects.filter(**{searchField + '__icontains': searchText}).values("applicationNumber","markFeature","applicationDate","registrationNumber","expiryDate","disclaimer","colors","verbalElements","owners_name","owners_address","owners_country","representatives_name","representatives_country","representatives_address","classifications_niceClass","classifications_goodServiceDescription")
            return render(request, 'import_site.html',{"pdf_instance":pdf_instance,"search": request.GET.get('searchText', ''),"search_1": request.GET.get('searchField', '')}) 
       
    return render(request, 'import_site.html')  # Replace 'your_template.html' with your actual template name