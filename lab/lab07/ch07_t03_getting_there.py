def hotel_cost(nights: int) -> int:
    return 140 * nights


def plane_ride_cost(city: str):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsbrgh":
        return 222
    elif city == "Los Angleles":
        return 475
    return "None"
