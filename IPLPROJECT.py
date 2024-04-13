# HEY I AM MAINAK THIS SIDE MAKINKG THIS PROGRAM FOR A SIMPLE  GAME OF CRICKET T20 TOURNAMENT
# THE PLAYERS WILL BE INPUT BY USER AND THEY CAN CHOSE BETWEEN DIFFERENT OPTIONS LIKE HEAD OR TAILS, RUNS OR OVERS ETC.
#SO AT FIRST I AM PRINING THE MATCH DETAILS.
Team_Name1= input("Enter the name of Team1: ")
Team_Name2= input("Enter the name of Team2: ")
Match_TIME = (input("Enter the starting time for the match (in 24-hour format): "))
Match_No = float(input("PLEASE ENTER THE NUMBER OF THE MATCH IN THIS TOURNAMENT: "  ))
To_Name = input("PLEASE ENTER THE NAME OF TOURNAMENT:")
over = int(input("PLEASE ENTER THE OVER INTHIS TOURNAMENT:" ))
print("WELCOME TO " + To_Name+ "CRICKET TOURNAMENT")
print("TODAY  THE MATCH WILL BE DELDING ON " + Match_TIME +  " UPWORDS BETWEEN " + Team_Name1 + "VS" + Team_Name2)

#HERE I AM TAKING A DICTIONARY NAMED playing_11a for team A 
palying_11a ={}
players_nameA01 = input( "ENTER THE NAME OF CAPTAIN IN TEAM A:")
players_nameA02 = input( "ENTER THE NAME OF VICE CAPTAIN IN TEAM A:")
players_nameA1 = input( "ENTER THE NAME OF  THE OPENNING STRIKER IN A TEAM:")
players_nameA2 = input( "ENTER THE NAME OF THE OPENNING NON STRIKER IN TEAM A:")
players_nameA3 = input( "ENTER THE NAME OF 3RD BATSMAN IN TEAM A:")
players_nameA4 = input( "ENTER THE NAME OF 4TH BATSMAN  IN TEAM A:")
players_nameA5 = input( "ENTER THE NAME OF THE WK IN TEAM A:")
players_nameA6 = input( "ENTER THE NAME OF BOWLER IN TEAM A:")
players_nameA7 = input( "ENTER THE NAME OF BOWLER IN TEAM A:")
players_nameA8 = input( "ENTER THE NAME OF BOWLER IN TEAM A:")
players_nameA9= input( "ENTER THE NAME OF BOWLER IN TEAM A:")
players_nameA10= input( "ENTER THE NAME OF ALLROUNDER IN TEAM A:")
players_nameA11= input( "ENTER THE NAME OF ALLROUNDER IN TEAM A:")
#ADDING THE PLAYERS INTO THE DICTIOANRY
palying_11a.update({"THE OPENNING STRIKER IN A TEAM:": " " + players_nameA1})
palying_11a.update({"THE OPENNING NON STRIKER IN A TEAM:": " " + players_nameA2})
palying_11a.update( {" 3RD BATTER IN TEAM A IS:"  : "-"+ players_nameA3})
palying_11a.update( {" 4TH BATSMAN IN TEAM A IS:": "-"+ players_nameA4})
palying_11a.update({"WK IN TEAM A IS:": " " + players_nameA5})
palying_11a.update({"BEST STEAM BOELER OF TEAM A IS:": " " + players_nameA6})
palying_11a.update({"IMPACTFUL STEAM BOELER OF TEAM A IS:": " " + players_nameA7})
palying_11a.update({" SPINNER BOELER OF TEAM A IS:": " " + players_nameA8})
palying_11a.update({"4TH  BOELER OF TEAM A IS:": " " + players_nameA9})
palying_11a.update({"NO1 ALLROUNDER OF TEAM A IS:": " " + players_nameA10})
palying_11a.update({"2ND ALLROUNDER OF TEAM A IS:": " " + players_nameA11})
palying_11a.update({"  TEAM A CAPTAIN IS:": " "+ players_nameA01 ,"AND  TEAM A VC IS:": " " + players_nameA02 })

#TEAM_A = {players_nameA1,players_nameA2,players_nameA3,players_nameA4,players_nameA5,players_nameA6,players_nameA7,players_nameA8,players_nameA9,players_nameA10,players_nameA11}
#HERE I AM TAKING AN ANOTHER DICTIONARY NAMED playing_11b for team B
playing_11b ={}
players_nameB01 = input( "ENTER THE NAME OF THE CAPTAIN IN TEAM B:")
players_nameB02 = input( "ENTER THE NAME OF THE VICE CAPTAIN IN TEAM B:")
players_nameB1 = input( "ENTER THE NAME OF THE OPENNING STRIKER IN TEAM B:")
players_nameB2 = input( "ENTER THE NAME OF THE OPENNING NON STRIKER IN TEAM B:")
players_nameB10 = input( "ENTER THE NAME OF THE FIRST ALLROUNDER IN TEAM B:")
players_nameB11 = input( "ENTER THE NAME OF THE SECOND ALLROUNDER IN TEAM B:")
players_nameB3 = input( "ENTER THE NAME OF 3RD BATSMAN IN TEAM B:")
players_nameB4 = input( "ENTER THE NAME OF 4TH BATSMAN  IN TEAM B:")
players_nameB5 = input( "ENTER THE NAME OF THE WK IN TEAM B:")
players_nameB6 = input( "ENTER THE NAME OF BOWLER IN TEAM B:")
players_nameB7 = input( "ENTER THE NAME OF BOWLER IN TEAM B:")
players_nameB8 = input( "ENTER THE NAME OF BOWLER IN TEAM B:")
players_nameB9= input( "ENTER THE NAME OF BOWLER IN TEAM B:")
#ADDING THE PLAYERS INTO THE DICTIONARY
playing_11b.update({"THE OPENNING STRIKER IN B TEAM:": " " + players_nameB1})
playing_11b.update({"THE OPENNING NON STRIKER IN B TEAM:": " " + players_nameB2}) 
playing_11b.update( {" 3RD BATTER IN TEAM B IS:"  : " "+ players_nameB3})
playing_11b.update( {" 4TH BATSMAN IN TEAM B IS:": " "+ players_nameB4})
playing_11b.update({"WK IN TEAM B IS:": " " + players_nameB5})
palying_11a.update({"BEST STEAM BOELER OF TEAM B IS:": " " + players_nameB6})
palying_11a.update({"IMPACTFUL STEAM BOELER OF TEAM B IS:": " " + players_nameB7})
palying_11a.update({" SPINNER BOELER OF TEAM B IS:": " " + players_nameB8})
palying_11a.update({"4TH  BOELER OF TEAM B IS:": " " + players_nameB9})
palying_11a.update({"NO1 ALLROUNDER OF TEAM B IS:": " " + players_nameB10})
palying_11a.update({"2ND ALLROUNDER OF TEAM B IS:": " " + players_nameB11})
#TEAM_B = {players_nameB1,players_nameB2,players_nameB3,players_nameB4,players_nameB5,players_nameB6,players_nameB7,players_nameB8,players_nameB9,players_nameB10,players_nameB11}
playing_11b.update({"  TEAM B CAPTAIN IS:": " "+ players_nameB01 ,"AND  TEAM B VC IS:": " " + players_nameB02 })
print("WELCOME TO " + To_Name+ "CRICKET TOURNAMENT")
print("TODAY  THE MATCH WILL BE DELDING ON " + Match_TIME +  " UPWORDS BETWEEN " + Team_Name1 + "VS" + Team_Name2)
print( "PLAYING 11 OF TEAM A ARE" ,palying_11a)
print("PLAYING 11 OF TEAM B ARE" , playing_11b)

class CricketMatch:
    def _init_(self):
        self.runs = 0
        self.wickets = 0
        self.wides = 0
        self.balls = 0
        self.player_scores = {'Player 1': 0, 'Player 2': 0}
        self.current_batsman = 'Player 1'
        self.team1_runs = 0
        self.team1_wickets = 0
        self.team2_runs = 0
        self.team2_wickets = 0
        self.bowler_stats = {'Team 1': {'runs': 0, 'wickets': 0}, 'Team 2': {'runs': 0, 'wickets': 0}}
        self.current_team = 'Team 1'

    def switch_batsman(self):
        if self.current_batsman == 'Player 1':
            self.current_batsman = 'Player 2'
        else:
            self.current_batsman = 'Player 1'

    def switch_team(self):
        if self.current_team == 'Team 1':
            self.current_team = 'Team 2'
        else:
            self.current_team = 'Team 1'

    def update_score(self, runs_scored, is_wide):
        self.balls += 1
        if is_wide:
            self.wides += 1
        else:
            self.runs += runs_scored
            self.player_scores[self.current_batsman] += runs_scored
            if self.current_team == 'Team 1':
                self.team1_runs += runs_scored
            else:
                self.team2_runs += runs_scored

    def update_wicket(self):
        self.wickets += 1
        self.switch_batsman()
        self.balls += 1
        if self.current_team == 'Team 1':
            self.team1_wickets += 1
        else:
            self.team2_wickets += 1

    def update_bowler_stats(self, runs_conceded, wicket_taken):
        if self.current_team == 'Team 1':
            self.bowler_stats['Team 2']['runs'] += runs_conceded
            self.bowler_stats['Team 2']['wickets'] += wicket_taken
        else:
            self.bowler_stats['Team 1']['runs'] += runs_conceded
            self.bowler_stats['Team 1']['wickets'] += wicket_taken

    def print_score(self):
        print(f"Ball {self.balls}: {self.runs} runs, {self.wickets} wickets, {self.wides} wide balls")
        print(f"{self.current_batsman} score: {self.player_scores[self.current_batsman]}")
        print(f"Team 1: {self.team1_runs}/{self.team1_wickets}")
        print(f"Team 2: {self.team2_runs}/{self.team2_wickets}")

    def print_total(self):
        print("\nMatch Summary:")
        print(f"Total runs scored: {self.runs}")
        print(f"Total wickets taken: {self.wickets}")
        print(f"Total wide balls: {self.wides}")
        print(f"Total balls bowled: {self.balls}")
        print("Player scores:")
        for player, score in self.player_scores.items():
            print(f"{player}: {score}")
        print("Bowler Stats:")
        for team, stats in self.bowler_stats.items():
            print(f"{team} - Runs: {stats['runs']}, Wickets: {stats['wickets']}")


def main():
    match = CricketMatch()

    while True:
        runs = input("Enter runs scored (press 'w' for wide, 'o' for over, 'e' for end): ")
        
        if runs.lower() == 'o':
            match.update_score(0, False)
            match.print_score()
            continue
        elif runs.lower() == 'e':
            match.print_total()
            break
        
        is_wide = False
        if runs.lower() == 'w':
            is_wide = True
            runs = 1  # Considering a wide delivery as 1 run
        
        try:
            runs = int(runs)
            if runs < 0:
                raise ValueError
        except ValueError:
            print("Invalid input! Please enter a non-negative integer or 'w' for wide, 'o' for over, 'e' for end.")
            continue

        match.update_score(runs, is_wide)
        match.print_score()


if _name_ == "_main_":
    main()
