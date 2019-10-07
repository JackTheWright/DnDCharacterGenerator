from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static

from . import poppdf

def character(request):
    url1 = 'static/charactersheet.pdf'
    url2 = 'character/static/newcharactersheet.pdf'
    poppdf.write_fillable_pdf(url1,
                              url2,
                              poppdf.data_dict)
    return render(request, 'character.html', {})
# Create your views here.
