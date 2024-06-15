from myapp.views import UserRegisterView, ShowWriters
from django.test import TestCase,Client  #class Client shabihsaze moroorgare request ersal mikone va response migire
from django.urls import reverse   #reverse bhsh url ro tahvil midi va path kamelesho bht mide
from django.contrib.auth.models import User
from myapp.forms import UserRegistrationForm
from myapp.models import Writer

class TestUserRegisterView(TestCase):
    def setUp(self):
        '''
            ye user misazim chon vaghti test anjam midim y database testi vasamon tashkil mide va
            nemishe k roo onai k darim az ghabl hesab koniim ydone bayad besazim
        '''
        self.client=Client()
        # User.objects.create_user(username='jahan' , email='jahan@jahan.com' , password='jahan')
        
        
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
        
        
    def test_user_register_valid_POST(self):
        '''
            check mikonim bbinim ke vaghti method post hastesh:
            * aya user tashkil mishe ya na az tarighe status code mifahmim 302 yani create user
            * be hamoon masiri k moshakhas kardim redirect mishe ya na bad az tashkile user.
            (redirectesh dorost kar mikone y na)
            
            * aya bad az inke methode post ejra shod, yedone user tashkil mishe ya na
        '''        
        url=reverse('myapp:register')
        
        response= self.client.post(url,data={'username':'tala' , 'email':'tala@tala.com' ,
                                             'password1':'talapass' , 'password2':'talapass'})
        
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('myapp:home'))
        self.assertEqual(User.objects.count(),1)
        
        
    
    def test_user_register_POST_invalid(self):
        '''
            * avalin test vaghti hast k data eshtebah behesh dadi va mibaret 
            bhet az dobare safe ro neshon mide darvaghe html vasat render mikone
            k form tooshe betooni dobare data vared koni pas status 200
            
            * check kardane inke template dorosti ro neshon mide ya na
            
            * mige bia check kon vaghti dari etelaate eshtebah vared mikoni age function 
            is_valid() behet true bargardoond bayad faild beshi (assertfalse bargardooni)
            
            * assertFormError yeki az option hay test django hastesh k errori k mikhay 
            bedi ro check mikone chon form ro khode django vasamon handle mikone va error
            esh roo default ineke ke `Enter a valid email address.` miaym check mikonim 
            bbinim vaghti be form moon data ghalat midim vaghean hamin error ro mide ya na
        '''
        
        url=reverse('myapp:register')
        response=self.client.post(url,data={'username':'ali' , 'email':'yeemaileshtebah' ,
                                             'password1':'alipass' , 'password2':'alipass'})  
        
        
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response,'form_register.html')
        self.assertFalse(response.context['form'].is_valid())
        self.assertFormError(response.context['form'] , 'email' , errors='Enter a valid email address.')
        
        
        
class TestShowWriter(TestCase):
    def setUp(self):
        self.client=Client()
        User.objects.create_user(username='ghazal' , email='ghazal@hafezi.com' , password='ghazal')
        self.client.login(username='ghazal' , email='ghazal@hafezi.com' , password='ghazal')

    def test_login_check(self):
        '''
            * vaghti ba method get miri y safe html i bht neshoon mide k mishe status code 200
            * address on template made nazar ro midim bhesh
        '''
        url=reverse('myapp:show_writers')
        response=self.client.get(url)
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , 'show_writers.html')
    
    