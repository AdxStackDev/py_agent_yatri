def checkMedium(travelMedium):

    if "flight" in travelMedium:
        return "flight"
    elif "bus" in travelMedium:
        return "bus"
    elif "flight" in travelMedium and "bus" in travelMedium:
        return ["flight", "bus"]
    else:
        return "...."