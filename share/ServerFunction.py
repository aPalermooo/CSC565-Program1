###################################
# Name:         ServerFunction.py
# Description:  Implementation of all the functionality expected of the server.
#               Server is responsible for taking in different quantities units of measurements for Distance, Weight, and Temperature
#                   and convert them between metric and imperial systems
#
# Author: Xander Palermo <ajp2s@missouristate.edu>
# Class: CSC565 - Computer Networking
# Assignment: Socket Programming Assignment 1
####################################

from share.Message import Message

# All conversion formulas are sourced from Google.com

def distance(value, is_metric) -> float:
    """
    Converts Kilometers to Miles
    :param value:       Value to be converted
    :param is_metric:   True is value is already in metric units
    :return: value in the opposite unit type ( Metric <--> Imperial )
    """
    if is_metric:
        return value / 1.609
    else:
        return value * 1.609

def weight(value, is_metric) -> float:
    """
    Converts Kilograms to Pounds
    :param value:       Value to be converted
    :param is_metric:   True is value is already in metric units
    :return: value in the opposite unit type ( Metric <--> Imperial )
    """
    if is_metric:
        return value * 2.205
    else:
        return value / 2.205


def temperature(value, is_metric)  -> float:
    """
    Converts Celsius to Fahrenheit
    :param value:       Value to be converted
    :param is_metric:   True is value is already in metric units
    :return: value in the opposite unit type ( Metric <--> Imperial )
    """
    if is_metric:
        return (value * (9 / 5)) + 32
    else:
        return (value - 32) * (9/5)



def convert(message : Message) -> Message | None:
    """
    Performs operations (conversions) requested by the client
    :param message: query to be operated on
    :return: a message containing queried item
    """
    """UNPACK MESSAGE"""
    message_type = message.header[0]
    is_metric = message.header[1]
    value = message.content

    """MATCH CONVERSION REQUESTED"""
    match message_type:
        case 1:
            value = distance(value, is_metric)
        case 2:
            value = weight(value, is_metric)
        case 3:
            value = temperature(value, is_metric)
        case _:
            value = None

    """ASSEMBLE RESPONSE AND RETURN"""
    return Message(header=(message_type, is_metric),
                   origin=message.destination,
                   destination=message.origin,
                   content=value)


def main():
    #TEST FUNCTIONALITY
    print(convert(Message((1, True), "localhost", "localhost", 5)))

if __name__ == "__main__":
    main()