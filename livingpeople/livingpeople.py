def getMostAliveDate(register):
    births = map(lambda dates: dates[0], register)

    births.sort()

    return births[0]
