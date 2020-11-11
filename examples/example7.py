winners = {}
# { 'Anaheim Angels': [2004, 2010], 'Chicago Cubs': [1906, 1907, 2016] }


def load_data():
    with open("WorldSeriesWinners.txt") as file:
        for year, team in enumerate(file, 1903):
            team = team.strip()
            if team not in winners:
                winners[team] = [year]
            else:
                winners[team].append(year)


def find_wins(team_name):
    if team_name in winners:
        print(team_name, "won the World Series in the following years:", end=" ")
        for year in winners[team_name]:
            print(year, end=" ")
        print()
    else:
        print("That team has not won any World Series.")


def main():
    load_data()
    while True:
        option = input("Enter a team name or 'q' to quit: ")
        if option.lower() == "q":
            break
        find_wins(option)


main()
