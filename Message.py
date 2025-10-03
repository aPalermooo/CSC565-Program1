from dataclasses import dataclass


@dataclass
class Message:
    header: str
    content: float
