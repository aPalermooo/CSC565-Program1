from dataclasses import dataclass



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
