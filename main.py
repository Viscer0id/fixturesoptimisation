from match import Match
from fixture import Fixture
from datetime import datetime
from random import choice
import csv

potential_matches = []
fixtures = []

print("Loading all potential matches")
with open('resources/all_potential_matches.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        potential_matches.append(Match(hometeam=row[1], awayteam=row[2], homevenue=row[3], preferredday=row[4], preferredtime=row[5], weight=int(row[6])))
print(len(potential_matches))

print("Loading all available spots")
with open('resources/all_available_spots.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        fixtures.append(Fixture(round=row[0], when=datetime.strptime(row[1]+" "+row[3],"%d/%m/%Y %H:%M"), venue=row[4], capacity=int(row[5])))
print(len(fixtures))

with open("resources/generated_fixtures.txt", mode='w', newline='', encoding='utf-8') as outfile:
    print("Randomly assign a potential match to an available spot i.e. create a fixture")
    for fixture in fixtures:    # Fill all available fixtures
        while fixture.available_capacity != 0:  # Fill all capacity for a given venue
            filtered_matches = list(filter(lambda x: x.homevenue == fixture.venue and x.weight <= fixture.available_capacity, potential_matches))   # Filter all potential matches for those that will fit the venue, and are the homegame for the venue

            if len(filtered_matches) > 0:   # We have some matches to choose from
                match = choice(filtered_matches)
                if int(fixture.available_capacity) >= int(match.weight):
                    fixture.matches.append(match)
                    fixture.available_capacity -= match.weight
            else:   # We do not have matches to choose from - this would be a "bye"
                break

        outfile.write(f"{fixture}")
        print(f"{fixture}")
