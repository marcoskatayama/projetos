import requests

HTTP_METHODS = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH", "TRACE"]

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def request(self, method, endpoint, data=None, headers=None, cookies=None):
        if not isinstance(method, str) or method.upper() not in HTTP_METHODS:
            raise ValueError("Invalid HTTP method")
        
        if not isinstance(data, dict) and (method in ["POST", "PUT"]):
            raise ValueError("Data must be a dictionary for POST and PUT requests")
        
        url = f"{self.base_url}/{endpoint}"
        
        if method == "GET":
            response = requests.get(url, data=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, cookies=cookies)
        elif method == "HEAD":
            response = requests.head(url, data=data, headers=headers, cookies=cookies)
        elif method == "OPTIONS":
            response = requests.options(url, data=data, headers=headers, cookies=cookies)
        elif method == "PATCH":
            response = requests.patch(url, json=data, headers=headers, cookies=cookies)
        elif method == "TRACE":
            response = requests.request(method="TRACE", url=url, data=data, headers=headers, cookies=cookies)
        else:
            raise ValueError("Invalid HTTP method")

        return response
