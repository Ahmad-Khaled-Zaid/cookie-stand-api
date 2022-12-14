from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Marshmello


class CookieTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser1.save()

        test_cookie = Marshmello.objects.create(
            location="USA",
            owner=testuser1,
            description="I like cookies",
            hourly_sales=1,
            minimum_customers_per_hour=10,
            maximum_customers_per_hour=1,
            average_cookies_per_sale=1.7

        )
        test_cookie.save()

    def setUp(self):
        self.client.login(username='testuser1', password="pass")

    def test_get_cookies_list_model(self):
        cookie = Marshmello.objects.get(id=1)
        actual_owner = str(cookie.owner)
        actual_location = str(cookie.location)
        actual_description = str(cookie.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_location, "USA")
        self.assertEqual(
            actual_description, "I like cookies"
        )

    def test_get_cookies_list(self):
        url = reverse("marshmello_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cookies = response.data
        self.assertEqual(len(cookies), 1)
        self.assertEqual(cookies[0]["owner"], 1)

    def test_auth_required(self):
        self.client.logout()
        url = reverse("marshmello_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("marshmello_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
