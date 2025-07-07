from dataclasses import dataclass

from demoga_test.enum.enum import Gender, Hobbies, State


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    year: str
    month: str
    day: str
    subject: str
    hobbies: Hobbies
    picture_name: str
    address: str
    state: State
    city: str

