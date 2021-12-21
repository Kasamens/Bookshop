from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

class HomePageTests(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_homepage_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(200, response.status_code)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_contains_correct_html(self):  
        response = self.client.get('/') 
        self.assertContains(response, 'Homepage')
    
    def test_homepage_does_not_contain_incorrect_html(self): 
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
    
    def test_homepage_url_resolves_homepageview(self): # new 
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
