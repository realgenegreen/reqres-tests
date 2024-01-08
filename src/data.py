from src.api import API
from src.webui import WEB

class Data:
    
    @staticmethod
    def for_api(sname='', param1:str=False, param2:str=False, param3:str=False):
        if sname == 'List users':
            return API.get_users(param1, param2)
        elif sname == 'Single user':
            return API.get_users(id=param1)
        elif sname == 'Single user not found':
            return API.get_users(id=param1)
        elif sname == 'List <resource>':
            return API.get_resource(param1, param2)
        elif sname == 'Single <resource>':
            return API.get_resource(id=param1)
        elif sname == 'Single <resource> not found':
            return API.get_resource(id=param1)
        elif sname == 'Create':
            return API.post_create(param1, param2)
        elif sname == 'Update PUT':
            return API.put_users(param1, [param2,param1, param3])
        elif sname == 'Update PATCH':
            return API.patch_users(param1, [param2,param1, param3])
        elif sname == 'Delete':
            return API.delete_users(id=param1)
        elif sname == 'Register - successful':
            return API.post_reg_log(param1, param2, param3, register=True)
        elif sname == 'Register - unsuccessful':
            return API.post_reg_log(param1, param2, param3, register=True)
        elif sname == 'Login - successful':
            return API.post_reg_log(param1, param2, param3, login=True)
        elif sname == 'Login - unsuccessful':
            return API.post_reg_log(param1, param2, param3, login=True)
        elif sname == 'Delayed response':
            return API.get_users(delay=param1)
        else:
            print('No corrrect arguments in <name>')
            return None


    @staticmethod
    def for_web(driver, name=''):
        if name == 'List users':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[1]')

        elif name == 'Single user':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[2]')

        elif name == 'Single user not found':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[3]')

        elif name == 'List <resource>':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[4]')

        elif name == 'Single <resource>':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[5]')

        elif name == 'Single <resource> not found':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[6]')

        elif name == 'Create':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[7]')

        elif name == 'Update PUT':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[8]')

        elif name == 'Update PATCH':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[9]')

        elif name == 'Delete':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[10]')

        elif name == 'Register - successful':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[11]')

        elif name == 'Register - unsuccessful':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[12]')

        elif name == 'Login - successful':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[13]')

        elif name == 'Login - unsuccessful':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[14]')

        elif name == 'Delayed response':
            return WEB.clicks(driver, '/html/body/div[2]/div/div/section[1]/div[1]/ul/li[15]', wait=3000)

        else:
            print('No corrrect arguments in <name>')
            return None





# ♥ for IBS with love ♥ #
