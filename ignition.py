import time

class Cars:
    def __init__(self):
        pass
    def ignition(self):
        print("Insert the key into the ignition/Press the ignition buttton")
        user = input('').capitalize().lower().strip()
        if user == 'start':
            print("Starting the engine...")
            time.sleep(4) 
            engine_status = "running..."
            if engine_status == "running...":
                print("The engine has started successfully!")
            time.sleep(2)
            print("The car is now ready to drive. Have a safe journey!")

        else: 
            print("Car failed to start!!!") 
mycar = Cars()
mycar.ignition()
  



