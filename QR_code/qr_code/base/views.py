from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
import io   
import qrcode.image.svg 
from django.conf import settings
from qrcode import *
import time

   
def qr_code(request): 
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(str(settings.MEDIA_ROOT) + '/' + img_name)
        
        return render(request, 'home.html', {'img_name': img_name})
    return render(request, 'home.html')


