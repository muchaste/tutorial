import sys

def check_temperature(temperature):
    print(temperature)
    if temperature > 30:
        print("too hot")
    elif temperature == 25:
        print("about right")
    else:
        print("cool")

temp = int(sys.argv[1])
check_temperature(temp)
