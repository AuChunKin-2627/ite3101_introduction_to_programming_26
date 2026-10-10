def shut_down(s: str) -> str:
    if s == "yes":
        return ("Shutting down")
    elif s == "no":
        return ("Shutdown abourted")
    else:
        return ("Sorry")
