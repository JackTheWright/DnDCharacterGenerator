from django.shortcuts import render
from django.http import HttpResponse
from . import poppdf

def character(request):
    pdf = poppdf.pdf()
    pdf.write_fillable_pdf(pdf.CHARSHEET_PATH,
                              pdf.CHARSHEET_OUTPUT_PATH,
                              pdf.data_dict)
    return render(request, 'character.html', {})
# Create your views here.
