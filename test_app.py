from app import app
from unittest import TestCase


class Tests(TestCase):

    def test_home_route(self):
        """This tests the main route checking for some of the form HTML"""
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertIn('id="form"', html)

    def test_valid_convert_route(self):
        """Tests to see if convert is working; 1 USD should equal 1 USD"""
        with app.test_client() as client:
            resp = client.get(
                '/convert', query_string=dict(user_from='USD', user_to='USD', user_amount="1"))
            html = resp.get_data(as_text=True)
            self.assertIn('The result is US$ 1.0.', html)

    def test_missing_from_convert_route(self):
        """Tests to see case of missing FROM currency"""
        with app.test_client() as client:
            resp = client.get(
                '/convert', query_string=dict(user_from='', user_to='USD', user_amount="1"))
            html = resp.get_data(as_text=True)
            self.assertIn(
                'Enter a valid &#39;FROM&#39; currency; &#39;&#39; is not a valid currency code.', html)

    def test_missing_to_convert_route(self):
        """Tests to see case of missing TO currency"""
        with app.test_client() as client:
            resp = client.get(
                '/convert', query_string=dict(user_from='USD', user_to='', user_amount="1"))
            html = resp.get_data(as_text=True)
            self.assertIn(
                'Enter a valid &#39;TO&#39; currency; &#39;&#39; is not a valid currency code.', html)

    def test_missing_amount_convert_route(self):
        """Tests to see case of missing amount"""
        with app.test_client() as client:
            resp = client.get(
                '/convert', query_string=dict(user_from='USD', user_to='USD', user_amount=""))
            html = resp.get_data(as_text=True)
            self.assertIn(
                'Enter a valid number.', html)

    def test_invalid_from_convert_route(self):
        """Tests to see case of invalid FROM currency"""
        with app.test_client() as client:
            resp = client.get(
                '/convert', query_string=dict(user_from='XXX', user_to='USD', user_amount="1"))
            html = resp.get_data(as_text=True)
            self.assertIn(
                '&#39;XXX&#39; is not a valid currency code.', html)

    def test_invalid_to_convert_route(self):
        """Tests to see case of invalid TO currency"""
        with app.test_client() as client:
            resp = client.get(
                '/convert', query_string=dict(user_from='USD', user_to='XXX', user_amount="1"))
            html = resp.get_data(as_text=True)
            self.assertIn(
                '&#39;XXX&#39; is not a valid currency code.', html)

    def test_invalid_amount_convert_route(self):
        """Tests to see case of invalid amount (not a number)"""
        with app.test_client() as client:
            resp = client.get(
                '/convert', query_string=dict(user_from='USD', user_to='USD', user_amount="cat"))
            html = resp.get_data(as_text=True)
            self.assertIn(
                'Enter a valid number.', html)
