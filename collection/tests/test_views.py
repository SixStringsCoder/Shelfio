from django.test import RequestFactory

from collection.views import home

class TestHome:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = home(req)
        assert resp.status_code == 200, 'Let this page be viewed by anyone'