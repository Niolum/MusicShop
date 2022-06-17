from django.test import TestCase
from ..models import Review
from django.urls import reverse


class ReviewCreateFormTest(TestCase):
    fixtures = ['product.json', 'user.json']

    def test_create_review(self):
        review_count = Review.objects.count()
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.post(reverse('add_review', args=['fender_am_pro_ii_tele_mn_bk']), { 'text':'cool',})
        self.assertRedirects(resp, '/products/fender_am_pro_ii_tele_mn_bk/')
        self.assertEqual(Review.objects.count(), review_count+1)
        self.assertTrue(Review.objects.filter(text='cool'))