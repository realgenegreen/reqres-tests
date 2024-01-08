from src.http_methods import Method

base_url = 'https://reqres.in/api/'

class API:

    @staticmethod
    def get_resource(page:str=False, per_page:str=False, id:str=False, delay:str=False):
        if id:
            url = base_url+'{resource}/'+id
        else:
            if page and per_page:
                url = base_url+'{resource}?page='+page+'&per_page='+per_page
            elif page:
                url = base_url+'{resource}?page='+page
            else:
                url = base_url+'{resource}'
        return Method.GET(url)if not delay else Method.GET(url+'?delay='+delay)

    @staticmethod
    def get_users(page:str=False, per_page:str=False, id:str=False, delay:str=False):
        if id:
            url = f'{base_url}users/{id}'
        else:
            if page and per_page:
                url = f'{base_url}users?page={page}&per_page={per_page}'
            elif page:
                url = f'{base_url}users?page={page}'
            else:
                url = f'{base_url}users'
        return Method.GET(url) if not delay else Method.GET(url+'?delay='+delay)
            
    @staticmethod
    def put_users(id='{id}', values:list='', delay:str=False):
        url = base_url+'users/'+id
        keys = {'name':None, 'job':None}
        body = {key:value for key, value in zip(keys, values)}
        return Method.PATCH(url, body)if not delay else Method.PATCH(url+'?delay='+delay, body)
    @staticmethod
    def put_resource(id='{id}', values:list='', delay:str=False):
        url = base_url+'{resource}/'+id
        keys = {'name':None, 'job':None}
        body = {key:value for key, value in zip(keys, values)}
        return Method.PUT(url, body)if not delay else Method.PUT(url+'?delay='+delay, body)

    @staticmethod
    def patch_users(id='{id}', values:list='', delay:str=False):
        url = base_url+'{resource}/'+id
        keys = {'name':None, 'job':None}
        body = {key:value for key, value in zip(keys, values)}
        return Method.PATCH(url, body)if not delay else Method.PATCH(url+'?delay='+delay, body)

    @staticmethod
    def patch_resource(id='{id}', body='', delay:str=False):
        url = base_url+'{resource}/'+id
        return Method.PATCH(url, body)if not delay else Method.PATCH(url+'?delay='+delay, body)

    @staticmethod
    def post_reg_log(username:str, email:str, password:str, register:bool=False, login:bool=False, logout:bool=False, delay:str=False):
        if register:
            url = f'{base_url}register'
            body = {
                    "username": username,
                    "email": email,
                    "password": password
                    }
        elif login:
            url = f'{base_url}login'
            body = {
                    "username": username,
                    "email": email,
                    "password": password
                    }
        elif logout:
            url = f'{base_url}logout'
            body = ''
        else:
            print('POST method has no register/login arguments')
            pass
        return Method.POST(url, body)if not delay else Method.POST(url+'?delay='+delay, body)

    @staticmethod
    def post_create(uname:str, ujob:str, delay:str=False):
        url = f'{base_url}users'
        body = {"name": uname, "job": ujob}
        return Method.POST(url, body)if not delay else Method.POST(url+'?delay='+delay, body)

    @staticmethod
    def delete_users(id='{id}', delay:str=False):
        url = f'{base_url}users/{id}'
        return Method.DELETE(url)if not delay else Method.DELETE(url+'?delay='+delay)

    @staticmethod
    def delete_resource(id='{id}', delay:str=False):
        url = base_url+'{resource}/'+id
        return Method.DELETE(url)if not delay else Method.DELETE(url+'?delay='+delay)



    # ♥ for IBS with love ♥ #
