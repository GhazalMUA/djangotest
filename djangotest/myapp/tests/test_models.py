from myapp.models import Writer
from django.test import TestCase
from model_bakery import baker

"""
    method setUp , ghabl az har method ejra mishe va ye kario
    anjam mide vase inke code mon tamiz tar va herfei tar bashe
    tashkile ye nevisandeye jadid ro tooye setup anjam midiim.
    vaseye inke momkene har model 20 ta field dashte bashe va
    ma vase test cfaghat b yeki dotashj niaz dashte bashimk va
    vaghgtemon heyf nashe vase por kardane baghie field hayi k 
    bhshon niazi nadarim, bayad az package pythoni be esme bakery 
    estefade konim. bayad aval nasbesh konim bad mesle zir azash
    estefade konim hala ma inja faghat mikhaym def str ro check
    konim k be firstname va lastname mortabete va baghie field 
    haro mikhaym k bakery vasamoon kossher por kone
"""

class TestwriterModel(TestCase):
    def setUp(self) -> None:
        self.writer = baker.make(Writer,first_name='amir' , last_name='hatami')
    
    def test_check_str(self):
        self.assertEqual(str(self.writer),'amir - hatami')