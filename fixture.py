

class Fixture:
    def __init__(self, round, when, venue, capacity):
        self.round = round
        self.when = when
        self.venue = venue
        self.total_capacity = capacity
        self.available_capacity = capacity
        self.matches = []
        self.matchesstring = ""

    def printMatches(self):
        for match in self.matches:
            self.matchesstring += f"{match.hometeam} vs. {match.awayteam}, "

    def __str__(self):
        self.printMatches()
        return "Round: %s, When: %s, Venue: %s, Total capacity: %s, Available capacity: %s, Matches: %s" % (self.round, self.when, self.venue, self.total_capacity, self.available_capacity, self.matchesstring)
