from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from . import poppdf

def character(request):
    url1 = staticfiles_storage.url('character/charactersheet.pdf')
    url2 = staticfiles_storage.url('character/newcharactersheet.pdf')
    poppdf.write_fillable_pdf(url1,
                              url2,
                              poppdf.data_dict)
    return render(request, 'character.html', {})
# Create your views here.
