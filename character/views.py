from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static
import os

from . import poppdf

def character(request):
    url1 = 'static/charactersheet.pdf'
    url2 = 'static/newcharactersheet.pdf'
    poppdf.write_fillable_pdf(url1,
                              url2,
                              poppdf.data_dict)
    print(os.path.abspath('character.html'))
    print(os.path.abspath('newcharactersheet.pdf'))
    print(os.listdir("/app/static/character"))
    return render(request, 'character.html', {})
# Create your views here.
