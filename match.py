class Match:
    def __init__(self, hometeam, awayteam, homevenue, preferredday, preferredtime, weight):
        self.hometeam = hometeam
        self.awayteam = awayteam
        self.homevenue = homevenue
        self.preferredday = preferredday
        self.preferredtime = preferredtime
        self.weight = weight

    def __str__(self):
        return "Hometeam: %s, Awayteam: %s, Venue: %s, Preferred day: %s, Preferred time: %s, Match weight: %s" % (self.hometeam, self.awayteam, self.homevenue, self.preferredday, self.preferredtime, self.weight)
