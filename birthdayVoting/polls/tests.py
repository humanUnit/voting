from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.test import RequestFactory
from django.test import TransactionTestCase


class UserHistoryTest(TransactionTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@mail.com', password='top_secret')

    def test_login(self):
        request = self.factory.get('polls:login')
        request.user = self.user
        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            print "okay"
