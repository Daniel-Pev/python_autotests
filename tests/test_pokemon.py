import requests

from common.conf import Cgf


def test_get_trainers():
    response = requests.get(url=Cgf.URL + '/trainers', params={'trainer_id': Cgf.TRAINER_ID}, headers=Cgf.HEADERS)
    assert response.status_code == 200, 'Unexpected statuscode'
    assert response.json()['data'][0]['id'] == str(Cgf.TRAINER_ID), 'Unexpected trainer id'
