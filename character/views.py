from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.staticfiles.finders import find

from . import poppdf

def character(request):
    url1 = find('/character/charactersheet.pdf')
    url2 = find('/character/newcharactersheet.pdf')
    poppdf.write_fillable_pdf(url1,
                              url2,
                              poppdf.data_dict)
    return render(request, 'character.html', {})
# Create your views here.
