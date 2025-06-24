import requests

def call_service2():
    try:
        response = requests.get("http://localhost:5001/service2")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    
if __name__ == '__main__':
    print(call_service2())

    
