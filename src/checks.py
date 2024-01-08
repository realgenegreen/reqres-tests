import json
# from requests import Response

class Check:

    @staticmethod
    def status_code(name, status_code):
        if name == 'List users':
            assert str(status_code) == '200'
        elif name == 'Single user':
            assert str(status_code) == '200'
        elif name == 'Single user not found':
            assert str(status_code) == '404'
        elif name == 'List <resource>':
            assert str(status_code) == '200'
        elif name == 'Single <resource>':
            assert str(status_code) == '200'
        elif name == 'Single <resource> not found':
            assert str(status_code) == '404'
        elif name == 'Create':
            assert str(status_code) == '201'
        elif name == 'Update PUT':
            assert str(status_code) == '200'
        elif name == 'Update PATCH':
            assert str(status_code) == '200'
        elif name == 'Delete':
            assert str(status_code) == '204'
        elif name == 'Register - successful':
            assert str(status_code) == '200'
        elif name == 'Register - unsuccessful':
            assert str(status_code) == '400'
        elif name == 'Login - successful':
            assert str(status_code) == '200'
        elif name == 'Login - unsuccessful':
            assert str(status_code) == '400'
        elif name == 'Delayed response':
            assert str(status_code) == '200'

    @staticmethod
    def expected_keys(name, body):
        if name == 'List users':
            dump = str(json.dumps(body))
            keys = ['page', 'per_page', 'total', 'data', 'id', 'email', 'first_name', 'last_name', 'avatar', 'support', 'url', 'text']
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Single user':
            dump = str(json.dumps(body))
            keys = ['data', 'id', 'email', 'first_name', 'last_name', 'avatar', 'support', 'url', 'text']
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Single user not found':
            dump = str(json.dumps(body))
            keys = []
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'List <resource>':
            dump = str(json.dumps(body))
            keys = ['page', 'per_page', 'total', 'data', 'id', 'name', 'year', 'color', 'pantone_value', 'support', 'url', 'text']
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Single <resource>':
            dump = str(json.dumps(body))
            keys = ['data', 'id', 'name', 'year', 'color', 'pantone_value', 'support', 'url', 'text']
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Single <resource> not found':
            dump = str(json.dumps(body))
            keys = []
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Create':
            dump = str(json.dumps(body))
            keys = ['name', 'job', 'id', 'createdAt']
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Update PUT':
            dump = str(json.dumps(body))
            keys = ['updatedAt']
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Update PATCH':
            dump = str(json.dumps(body))
            keys = ['name', 'job', 'updatedAt']
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Delete':
            dump = str(json.dumps(body))
            keys = []
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Register - successful':
            dump = str(json.dumps(body))
            keys = ['id', 'token']
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Register - unsuccessful':
            dump = str(json.dumps(body))
            keys = ['error']
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Login - successful':
            dump = str(json.dumps(body))
            keys = ['token']
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Login - unsuccessful':
            dump = str(json.dumps(body))
            keys = ['error']
            assert all(key in dump for key in keys), 'Wrong keys!'
        elif name == 'Delayed response':
            dump = str(json.dumps(body))
            keys = ['page', 'per_page', 'total', 'data', 'id', 'email', 'first_name', 'last_name', 'avatar', 'support', 'url', 'text']
            assert all(key in dump for key in keys), 'Wrong keys!'



# ♥ for IBS with love ♥ #
