from django.test import SimpleTestCase
from django.urls import reverse , resolve
from bcbsoftwares.views import *

class TestUrls(SimpleTestCase):
    def test_bcb_index(self):
        url = reverse('bcb:index')
        self.assertEquals(resolve(url).func,bcbvideosoftware)

    def test_bcb_index(self):
        url = reverse('bcb:bcbprojectmanagment')
        self.assertEquals(resolve(url).func,bcbprojectmanagment)

    def test_bcb_index(self):
        url = reverse('bcb:bcbcrmsoftware')
        self.assertEquals(resolve(url).func,bcbcrmsoftware)

    def test_bcb_index(self):
        url = reverse('bcb:appointment')
        self.assertEquals(resolve(url).func,bcbappointmentsoftware)

    def test_bcb_index(self):
        url = reverse('bcb:bcbfilesharingsoftware')
        self.assertEquals(resolve(url).func,bcbfilesharing)

    def test_bcb_index(self):
        url = reverse('bcb:bcbaccountingsoftware')
        self.assertEquals(resolve(url).func,bcbaccountingsoftware)

    def test_bcb_index(self):
        url = reverse('bcb:bcbtextmarketing')
        self.assertEquals(resolve(url).func,bcbtextmarketing)

    def test_bcb_index(self):
        url = reverse('bcb:bcbvoice')
        self.assertEquals(resolve(url).func,bcbvoice)

    def test_bcb_index(self):
        url = reverse('bcb:bcbmarketingautomation')
        self.assertEquals(resolve(url).func,bcbmarketingautomation)

    def test_bcb_index(self):
        url = reverse('bcb:bcbwebsitebuilder')
        self.assertEquals(resolve(url).func,bcbwebsitebuilder)

    def test_bcb_index(self):
        url = reverse('bcb:bcbwebhosting')
        self.assertEquals(resolve(url).func,bcbwebhosting)

    def test_bcb_index(self):
        url = reverse('bcb:bcbseosoftware')
        self.assertEquals(resolve(url).func,bcbseosoftware)
