import threading 
import service1
import service2

def run_service2():
    service2.app.run(port=5001)

if __name__== '__main__':
    service2_thread = threading.Thread(target=run_service2)
    service2_thread.start()

    print(service1.call_service2())
    