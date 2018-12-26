from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.renderers import TemplateHTMLRenderer
from cat_dog.serializers import ImagesSerializer
from cat_dog.models import MyImages
import coreapi


class MyUploadView(generics.CreateAPIView):
    serializer_class = ImagesSerializer
    schema = AutoSchema(manual_fields=[
        coreapi.Field(
            "myfile",
            required=True,
            type="file"
        ),
    ])

    def post(self, request, *args, **kwargs):
        """
        Test image description.
        """
        return self.create(request, *args, **kwargs)

    