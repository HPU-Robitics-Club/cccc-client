from approxeng.input.selectbinder import ControllerResource
from time import sleep
import requests

hostname = "127.0.0.1"
port = 5000
IP = f'https://{hostname}:{port}'

previousX = 0.0
previousY = 0.0

def registerControllerListener():
    while True:
        # Checks to make sure joystick is connected
        try: 
            with ControllerResource() as joystick:
                print('Found joystick!')
                while joystick.connected:
                    x = joystick.rx
                    y = joystick.ry

                    if x == previousX and y == previousY:
                        res = requests.post(IP, {
                            "controller_x": x,
                            "controller_y": y
                        })

                        print(res.data())

                        previousX = x
                        previousY = y

        except IOError:
            print("Unable to find joystick!")
            sleep(1.0)
