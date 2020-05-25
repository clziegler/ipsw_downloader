import devicetypes
from pprint import pprint
import sys


def user_interface():
    device_list = []
    logo = """
=================================================================================================    
 _____ ______  _____  _    _  ______                          _                    _             
|_   _|| ___ \/  ___|| |  | | |  _  \                        | |                  | |            
  | |  | |_/ /\ `--. | |  | | | | | |  ___  __      __ _ __  | |  ___    __ _   __| |  ___  _ __ 
  | |  |  __/  `--. \| |/\| | | | | | / _ \ \ \ /\ / /| '_ \ | | / _ \  / _` | / _` | / _ \| '__|
 _| |_ | |    /\__/ /\  /\  / | |/ / | (_) | \ V  V / | | | || || (_) || (_| || (_| ||  __/| |   
 \___/ \_|    \____/  \/  \/  |___/   \___/   \_/\_/  |_| |_||_| \___/  \__,_| \__,_| \___||_|   
=================================================================================================                                                                                                 

Download the most recent IPSW for iPhone and iPad

"""
    print(logo)
    device_list = user_start()

    return device_list


def user_start():
    while True:
        answer = raw_input(
            "iOS device type:\n 1 : iPhone \n 2 : iPad \n (type 1, 2, or q to quit)\n User Choice: "
        )
        if answer == "q":
            sys.exit()
        elif answer == "1":
            device_list = show_iphones()
            break
        elif answer == "2":
            device_list = show_ipads()
            break
        else:
            print("I did't understand: {}".format(answer))
    return device_list


text = "Enter the model IPSWs that you wish to download, seperated by a comma and space ex: <iPhone 8, iPhone X>. \n Or type ALL to download all IPSWs\n Enter device models, ALL, BACK to go to previous screen or q to quit\n User Choice: "


def show_iphones():

    while True:
        for k, _ in devicetypes.iPhones.items():
            print(k)
        answer = raw_input(text)
        if answer == "q":
            sys.exit()
        elif answer == "BACK":
            user_start()
        elif answer == "ALL":
            device_list = devicetypes.iPhones.values()
            return device_list
        else:
            try:
                answer_list = answer.split(", ")
                newdict = {k: devicetypes.iPhones[k] for k in answer_list}
                device_list = newdict.values()
                return device_list
            except:
                print(
                    "No valid models were entered- please check spelling and capitaliztion."
                )


def show_ipads():
    while True:
        for k, _ in devicetypes.iPads.items():
            print(k)
        answer = raw_input(text)
        if answer == "q":
            sys.exit()
        elif answer == "BACK":
            user_start()
            break
        elif answer == "ALL":
            device_list = devicetypes.iPads.values()
            return device_list
        else:
            try:
                answer_list = answer.split(", ")
                newdict = {k: devicetypes.iPads[k] for k in answer_list}
                device_list = newdict.values()
                return device_list
            except:
                print(
                    "No valid models were entered- please check spelling and capitaliztion."
                )
