from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import cv2
import numpy as np
import matplotlib.image as image
from sklearn.cluster import MiniBatchKMeans
import os

# Create your views here.
def home(request):
    if(request.method == "POST"):
        image = request.FILES['img']
        cluster = int(request.POST['cluster'])
        fs = FileSystemStorage()
        name = fs.save(image.name,image)
        try:
            os.remove('static/compressed.jpg')
        except:
            print("Image not found")
        size = image_compress(name,cluster)
        urls = {'Original':'media/'+ name,'Compressed':'static/Compressed.jpg','download':'static/compressed.jpg'}
    else:
        urls = {'Original':'static/img/bird.jpg','Compressed':'static/img/bird_comp.jpg','download':'static/img/bird.jpg'}
        size = {'Original':120,'Compressed':84}
    return render(request,'home.html',{'urls':urls,'size':size})
        
def image_compress(name,cluster):
    img = cv2.imread('media/'+ name)

    if(len(img.shape) < 3):
        Z = (img/255).reshape((-1,1))
    elif(len(img.shape) == 3):
        Z = (img/255).reshape((-1,3))

    k = cluster
    kmeans = MiniBatchKMeans(k).fit(Z)

    k_colors = kmeans.cluster_centers_[kmeans.predict(Z)]
 
    k_img = np.reshape(k_colors, (img.shape))

    image.imsave('static/compressed.jpg',k_img)

    return {'Original':os.path.getsize('media/'+ name)*0.001,'Compressed':os.path.getsize('static/compressed.jpg')*0.001}




