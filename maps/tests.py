from django.test import TestCase
from django.contrib.auth.models import User
from .models import Location, LocationType


class LocationDeletionTests(TestCase):
    def setUp(self):
        # Creating test users
        self.user1 = User.objects.create_user(
            'user1', 'user1@example.com', 'password1')
        self.user2 = User.objects.create_user(
            'user2', 'user2@example.com', 'password2')

        # Creating a LocationType instance
        location_type = LocationType.objects.create(name='TestType')

        # Creating a location for each user
        self.location1 = Location.objects.create(
            user=self.user1,
            latitude=123.45,
            longitude=67.89,
            type=location_type  # Use the LocationType instance
        )
        self.location2 = Location.objects.create(
            user=self.user2,
            latitude=98.76,
            longitude=54.32,
            type=location_type  # Use the same LocationType instance
        )

    def test_user_can_delete_own_location(self):
        self.client.login(username='user1', password='password1')
        response = self.client.post(f'/delete_location/{self.location1.id}/')
        print(response)
        self.assertEqual(response.status_code, 302)

    def test_user_cannot_delete_others_location(self):
        self.client.login(username='user1', password='password1')
        response = self.client.post(f'/delete_location/{self.location2.id}/')
        print(response)
        self.assertEqual(response.status_code, 403)

    def test_anonymous_user_cannot_delete_location(self):
        response = self.client.post(f'/delete_location/{self.location1.id}/')
        print(response)
        self.assertNotEqual(response.status_code, 302)
