from django.shortcuts import render
from django.http import HttpResponse
from . import poppdf

def character(request):
    url1 = '/static/character/charactersheet.pdf'
    url2 = staticfiles_storage.url('character/newcharactersheet.pdf')
    poppdf.write_fillable_pdf(url1,
                              url2,
                              poppdf.data_dict)
    return render(request, 'character.html', {})
# Create your views here.
