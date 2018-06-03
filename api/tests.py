from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Origin, Character
from rest_framework import status
import tempfile


class OriginTestCase(TestCase):
    """ Test module for Origin model """

    def test_model_can_create_origin(self):
        """Test the origin model can create an origin."""
        old_count = Origin.objects.count()
        
        Origin.objects.create(name='Earth (C-137)')
        
        new_count = Origin.objects.count()
        self.assertNotEqual(old_count, new_count)
    

class CharacterTestCase(TestCase):
    """ Test module for Character model """

    def test_model_can_create_a_character(self):
        """Test the character model can create an character."""
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        old_count = Character.objects.count()
        origin = Origin.objects.create(name='Earth (C-137)')

        Character.objects.create(name='Rick Sánchez', origin=origin, image=image)
        
        new_count = Character.objects.count()
        self.assertNotEqual(old_count, new_count)
        
        
    def test_created_character_has_origin(self):
        """Test the created character has origin."""
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        origin = Origin.objects.create(name='Earth (C-137)')

        Character.objects.create(name='Rick Sánchez', origin=origin, image=image)
        
        character = Character.objects.get(name='Rick Sánchez')
        self.assertEqual(origin.name, character.origin.name)


class OriginAPITestCase(APITestCase):
    """ Test module for Origin api """

    def test_api_can_create_origin(self):
        """Test the origin api can create an origin."""
        url = reverse('origin-list')
        data = {'name': 'Earth (C-137)'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Origin.objects.count(), 1)
        self.assertEqual(Origin.objects.get().name, 'Earth (C-137)')
