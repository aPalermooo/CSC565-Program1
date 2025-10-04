###################################
# Name:         Message.py
# Description:  A Data class that groups information so it can easily be sent between client and server
#
# Author: Xander Palermo <ajp2s@missouristate.edu>
# Class: CSC565 - Computer Networking
# Assignment: Socket Programming Assignment 1
####################################
import json
from dataclasses import dataclass, asdict

# Maps MessageType to units it is converting between (Metric, Imperial)

OPTIONS = {"Exit": None,
               "Distance": ("Kilometers", "Miles"),
               "Weight": ("Kilograms", "Pounds"),
               "Temperature": ("Celsius", "Fahrenheit")}

@dataclass
class Message:
    """
    A data class that contains all information to be transferred between server and client

    header (MessageType, isMetricToImperial)

    origin The IP address of the creator of the message

    destination The IP address of the intended recipient of the message

    content: computed value


    Message Type is described as follows:
    1. Request Distance
    2. Request Weight
    3. Request Temperature
    """
    header: tuple[int,bool]
    origin: str
    destination: str
    content: float


def main():
    #Test Functionality
    print("Hello World")


if __name__ == "__main__":
    main()