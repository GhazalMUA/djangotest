'''
    mamolan field hay form ro test nmikonim chon django khodesh khoob testeshon
    mikone ma faghat methodhaye tooye har class form moon ro test mikonim.
'''

from myapp.forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.test import TestCase



class TestRegistratonForm(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='nastaran', 
                                 email='nastaran@nastaran.com'
                                 ,password='nastaran')
    
    
    def test_valid_input(self):
        #in test mige age hameye etelaat dorost vared shode boodan
        # bayad true bargardooni ebarate form.is_valid() ro.
        form=UserRegistrationForm(data={'username':'behrad',
                                        'email':'behrad@gmail.com',
                                        'password1':'behrad' ,
                                        'password2':'behrad'})
        self.assertTrue(form.is_valid())
        
        
    def test_empty_input(self):
        #age etelaat ro tooye form hichi nafrestim ham form.is_valid 
        # ro bayad bhmoon false bargardoone ham inke bayad
        #behemon 4ta error bargardone(chon formemoon 4ta field dare.)
        form=UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),4)       
    

    def test_unrepeted_email(self):
        #aval bayad y obj ijad konim tooye datbase ke ye email
        # moshakhas dashte bashe k badan ke tooye form data ba 
        # email tekrari ferestadim bhmon khata bede.
        #on user ro tooye method setuptestdata mizaram.khate akhare
        # in function hm mige eroor dafre form v too bakhshe email hastesh
        form=UserRegistrationForm(data={'username':'nahid' ,
                                        'email':'nastaran@nastaran.com' ,
                                        'password1':'nahid' , 
                                        'password2':'nahid'})
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('emial'))
    
    
    
    def test_unmatched_passwords(self):
        #dota pass mokhtalef midim heyne tashkile ye for. bayad ham
        # yedone eroor behemon bede va ham error dashtan ro true bargardone
        #nokteye mohem ine ke mesle ghabi nmitonim bgim toye che fieldi error hast 
        #too function ghabli goftim ke tooye field email moshkel hastesh vali inja 
        #chon method clean ro tooye form override karde bdoim(hamoon mehtodi ke check
        # mikard bbine dota pass baham barabar hastan ya na.) in be kole form barmigardoone 
        # vase hmin nmitoonim esme y field khas ro biarim
        
        form=UserRegistrationForm(data={'username':'ahmad' ,
                                        'email':'ahmad@ahmad.com' , 
                                        'password1':'ahmad' , 
                                        'password2':'ahmadddd'
                                        })
        self.assertEqual(len(form.errors),1)
        self.assertTrue(form.has_error)