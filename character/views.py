from django.shortcuts import render
from django.http import HttpResponse
import poppdf

def character(request):
    poppdf.write_fillable_pdf(poppdf.CHARSHEET_PATH,
                              poppdf.CHARSHEET_OUTPUT_PATH,
                              poppdf.data_dict)
    return render(request, 'character.html', {})
# Create your views here.
