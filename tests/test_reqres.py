import pytest
from requests import Response
from src.data import Data
from src.checks import Check

@pytest.fixture(params=['List users',
                        'Single user',
                        'Single user not found',
                        'List <resource>',
                        'Single <resource>',
                        'Single <resource> not found',
                        'Create',
                        'Update PUT',
                        'Update PATCH',
                        'Delete',
                        'Register - successful',
                        'Register - unsuccessful',
                        'Login - successful',
                        'Login - unsuccessful',
                        'Delayed response'])
def names(request):
    yield request.param


class TestAPI:

    @staticmethod
    # @pytest.mark.skip()
    @pytest.mark.parametrize(('name', 'param1', 'param2', 'param3'),
                             [('List users', '2', '6', False),
                              ('Single user', '2', False, False),
                              ('Single user not found', '23', False, False),
                              ('List <resource>', '1', '6', False),
                              ('Single <resource>', '2', False, False),
                              ('Single <resource> not found', '23', False, False),
                              ('Create', 'morpheus', 'leader', False),
                              ('Update PUT', '2', 'morpheus','zion resident'),
                              ('Update PATCH', '2', 'morpheus','zion resident'),
                              ('Delete', '2', False, False),
                              ('Register - successful', None, 'eve.holt@reqres.in', 'pistol'),
                              ('Register - unsuccessful', None, None, 'pistol'),
                              ('Login - successful', None, 'eve.holt@reqres.in', 'cityslicka'),
                              ('Login - unsuccessful', None, 'eve.holt@reqres.in', None),
                              ('Delayed response', '3', False, False)])
    def test_api(name, param1, param2, param3):
        request: Response = Data.for_api(name, param1, param2, param3)
        Check.status_code(name, request.status_code)
        Check.expected_keys(name, request.text)

class TestWEB:

    @staticmethod
    # @pytest.mark.skip()
    def test_web(driver, names):
        click = Data.for_web(driver, names)
        Check.status_code(names, click['status_code'])
        Check.expected_keys(names, click)



# ♥ for IBS with love ♥ #
