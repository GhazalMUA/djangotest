from myapp.views import UserRegisterView, ShowWriters
from django.test import TestCase , Client     #class Client shabihsaze moroorgare request ersal 
                                              #mikone va response migire
                                              
from django.urls import reverse       #reverse bhsh url ro tahvil midi va path kamelesho bht mide
from django.contrib.auth.models import User
from myapp.forms import UserRegistrationForm

class TestUserRegisterView(TestCase):
    def setUp(self):
        '''
            ye user misazim chon vaghti test anjam midim y database testi vasamon tashkil mide va
            nemishe k roo onai k darim az ghabl hesab koniim ydone bayad besazim
        '''
        self.client=Client()
        User.objects.create_user(username='jahan' , email='jahan@jahan.com' , password='jahan')
        
        
    def test_user_register_GET(self):
        '''
           * karbar form ro dare mibine pas ye html dare vasash render mishe ba status code 200
           * karbar dare formi k tooye 'form_register.html' hast ro mibine
           * ye form dare ba context az view ersal mishe be html
        '''
        url= reverse('myapp:register')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'form_register.html')
        self.assertIsInstance(response.context['form'], UserRegistrationForm)
        