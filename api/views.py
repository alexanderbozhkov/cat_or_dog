from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from api.forms import UploadFileForm
import requests


def index(request, **kwargs):
    return render(request, "homepage.html", {"is_homepage": True, "is_upload_image": False, "is_draw_image": False})


@csrf_exempt
def upload_image_template(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = {
                "myfile": form.data['title'],
                "title": form.files['file']
            }
            headers = {'Accept': 'multipart/form-data'}
            response = requests.post("http://127.0.0.1:8000/api/images/upload/", data=data, headers=headers)
            print('@@@@: ', response)
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()

    content = {"form": form, "is_homepage": False, "is_upload_image": True, "is_draw_image": False}
    return render(request, "homepage.html", content)


def draw_image_template(request, **kwargs):
    return render(request, "homepage.html", {"is_homepage": False, "is_upload_image": False, "is_draw_image": True})


# TODO: probably delete, I won't need this

# def handle_uploaded_file(file):
# #    logging.debug("upload_here")
#     if file:
#         destination = open('/tmp/'+file.name, 'wb+')
#         #destination = open('/tmp', 'wb+')
#         for chunk in file.chunks():
#             destination.write(chunk)
#         destination.close()