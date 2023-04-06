from django.test import TestCase
from django.urls import reverse
from AppCoder.models import Destino

# Create your tests here.

class DestinoTestCase(TestCase):
    def setUp(self):
        Destino.objects.create(titulo="Cerdeña", descripcion="Italia")
        Destino.objects.create(titulo="Santorini", descripcion="Grecia")

    def test_creando_destinos(self):
        p1=Destino.objects.get(descripcion="Italia")
        p2=Destino.objects.get(descripcion="Grecia")
        self.assertEqual(p1.titulo, 'Cerdeña')
        self.assertEqual(p2.titulo, 'Santorini')

class ViewTests(TestCase):
    def test_no_questions(self):
        response=self.client.get(reverse('AppCoderDestinos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Creacion del destino")

