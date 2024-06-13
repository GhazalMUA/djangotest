from django.test import TestCase 
from django.urls import reverse,resolve
from myapp.views import HomeView,AboutView

class TestUrls(TestCase):
    def test_home(self):
        url=reverse('myapp:home')
        self.assertEqual(resolve(url).func.view_class , HomeView)