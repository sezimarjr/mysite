import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    reponse = client.get(url)
    assert reponse.status_code == 200
    assert reponse.content == b'Hello, world.'
