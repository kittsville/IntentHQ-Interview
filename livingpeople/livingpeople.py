def getMostAliveDate(dates):
    births = map(lambda life: life[0], dates)

    births.sort()

    return births[0]
