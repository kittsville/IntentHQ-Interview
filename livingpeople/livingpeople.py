class Event:
    def __init__(self, year):
        self.year = year

    def __repr__(self):
        return "{}@{}".format(self.__class__.__name__, self.year)

class Birth(Event):
    pass

class Death(Event):
    pass

def sortDates(firstDate, secondDate):
    """
        Orders births before deaths in the same year
    """
    if firstDate.year == secondDate.year:
        firstIsBirth  = isinstance(firstDate, Birth)
        secondIsBirth = isinstance(secondDate, Birth)

        if firstIsBirth and secondIsBirth:
            return 0
        elif firstIsBirth:
            return -1
        else:
            return 1
    else:
        return firstDate.year - secondDate.year

def getMostAliveYear(register):
    events = []

    for dates in register:
        events.append(Birth(dates[0]))
        events.append(Death(dates[1]))

    events.sort(cmp = sortDates)

    mostAliveYear = 1900
    mostAlive     = 0
    currentAlive  = 0

    for lifeEvent in events:
        if isinstance(lifeEvent, Birth):
            currentAlive += 1

            if currentAlive > mostAlive:
                mostAlive     = currentAlive
                mostAliveYear = lifeEvent.year
        else:
            currentAlive -= 1

    return mostAliveYear
