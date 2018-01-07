class Event:
    def __init__(self, year):
        self.year = year

    def __repr__(self):
        return "{}@{}".format(self.__class__.__name__, self.year)

class Birth(Event):
    pass

class Death(Event):
    pass

def getMostAliveDate(register):
    events = []

    for dates in register:
        events.append(Birth(dates[0]))
        events.append(Death(dates[1]))

    events.sort(key = lambda date: date.year)
    
    mostAliveDate = 1900
    mostAlive     = 0
    currentAlive  = 0

    for lifeEvent in events:
        if isinstance(lifeEvent, Birth):
            currentAlive += 1

            if currentAlive > mostAlive:
                mostAlive     = currentAlive
                mostAliveDate = lifeEvent.year
        else:
            currentAlive -= 1

    return mostAliveDate
