from django.test import TestCase
from django.urls import reverse


class CategoryListViewTest(TestCase):
    fixtures = ['product.json', 'user.json']

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'product/category_list.html')

    
class SubcategoryCategoryListViewTest(TestCase):
    fixtures = ['product.json', 'user.json']

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/categories/guitar_and_basses/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('categories', args=['guitar_and_basses']))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('categories', args=['guitar_and_basses']))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'product/subcategory_list.html')


class ProductSubcategoryListViewTest(TestCase):
    fixtures = ['product.json', 'user.json']

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/subcategories/electric_guitars/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('subcategories', args=['electric_guitars']))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('subcategories', args=['electric_guitars']))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'product/product_list.html')

    def test_pagination_is_three(self):
        resp = self.client.get(reverse('subcategories', args=['electric_guitars']))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['product_list']) == 3)

    def test_lists_all_products(self):
        resp = self.client.get(reverse('subcategories', args=['electric_guitars'])+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['product_list']) == 3)


class ProductDetailViewTest(TestCase):
    fixtures = ['product.json', 'user.json']

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/products/fender_am_pro_ii_tele_mn_bk/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('products', args=['fender_am_pro_ii_tele_mn_bk']))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('products', args=['fender_am_pro_ii_tele_mn_bk']))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'product/product_detail.html')
    
    def test_view_addreview(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.post(reverse('add_review', args=['fender_am_pro_ii_tele_mn_bk']), { 'text':'cool',})
        self.assertRedirects(resp, '/products/fender_am_pro_ii_tele_mn_bk/')