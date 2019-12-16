from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static
import os

from . import poppdf

def generate(request):
    url1 = 'static/charactersheet.pdf'
    url2 = 'static/character/newcharactersheet.pdf'
    level = request.body.decode("utf-8")
    print(level)
    poppdf.write_fillable_pdf(url1,
                              url2,
                              poppdf.data_dict, int(level))
    print(os.path.abspath('character.html'))
    print(os.path.abspath('newcharactersheet.pdf'))
    print(os.listdir("/app/static/character"))
    return HttpResponse("character generated.")

def download(request):
        return render(request, 'character.html', {})

# Create your views here.
