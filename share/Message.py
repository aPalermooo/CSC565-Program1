from dataclasses import dataclass



OPTIONS = {"Exit": None,
               "Distance": ("Kilometers", "Miles"),
               "Weight": ("Kilograms", "Pounds"),
               "Temperature": ("Celsius", "Fahrenheit")}

@dataclass
class Message:
    """
    A data class that contains all information to be transferred between server and client
    Header: (MessageType, isMetricToImperial)
    content: computed value


    Message Type is described as follows:
    0. Response
    1. Request Distance
    2. Request Weight
    3. Request Temperature
    """
    header: tuple[int,bool]
    content: float
