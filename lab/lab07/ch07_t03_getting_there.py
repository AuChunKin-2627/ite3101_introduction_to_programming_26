from typing import Any


def hotel_cost(nights: int) -> int:
    return 140 * nights


def plane_ride_cost(city: str)->Any:
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angleles":
        return 475
    elif city == "":
        return "None"


print(plane_ride_cost(""))
