import requests

class Method:
    headers = {'accept':'application/json'}

    @staticmethod
    def GET(url):
        return requests.get(url, headers=Method.headers, cookies='', timeout=50)
    
    @staticmethod
    def POST(url, body):
        return requests.post(url, json=body, headers=Method.headers, cookies='', timeout=50)
    
    @staticmethod
    def PUT(url, body):
        return requests.put(url, json=body, headers=Method.headers, cookies='', timeout=50)
    
    @staticmethod
    def PATCH(url, body):
        return requests.patch(url, json=body, headers=Method.headers, cookies='', timeout=50)
    
    @staticmethod
    def DELETE(url):
        return requests.delete(url, headers=Method.headers, cookies='', timeout=50)



# ♥ for IBS with love ♥ #
