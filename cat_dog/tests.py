from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Images
from .serializers import ImagesSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_image(name="", predict_score=""):
        if name != "" :
            Images.objects.create(name=name, predict_score=(predict_score if predict_score else None))

    def setUp(self):
        # add test data
        self.create_image("cat.png", "99.99")
        self.create_image("dog.png", "88,88")
        self.create_image("lizzard.png")


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("images-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Images.objects.all()
        serialized = ImagesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
