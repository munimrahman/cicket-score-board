import random

class T2Cup:
    all_teams = []
    def entry_team(self, team):
        self.all_teams.append(team)

class Team(T2Cup):
    def __init__(self, name) -> None:
        self.team_name = name
        self.players_list_obj = []
        super().entry_team(self)
    def entry_player(self, player):
        self.players_list_obj.append(player)
    def __repr__(self) -> str:
        return f'{self.team_name}'

class Player:
    def __init__(self, name, team_obj) -> None:
        self.player_name = name
        self.strike_rate = 0.0
        self.run_bat = 0
        self.ball_used = 0
        self.run_ball = 0
        self.wicket_taken = 0
        self.fours = 0
        self.sixes = 0
        self.balls_bowled = 0
        team_obj.entry_player(self)

    def __repr__(self) -> str:
        return f'{self.player_name}'

class Innings:
    def __init__(self, team1, team2, batting_team, bowling_team) -> None:
        self.team_one = team1
        self.team_two = team2
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.total_run = 0
        self.total_wicket = 0
        self.total_over = 0
        self.current_ball = 0
        self.current_batting_list = [batting_team.players_list_obj[0], batting_team.players_list_obj[1]]
        self.striker = batting_team.players_list_obj[0]
        self.current_bowler = None
        self.current_over_status = []
        self.all_over_status = []
    def show_score_board(self):
        print(f'{self.current_batting_list[0].player_name}* - {self.current_batting_list[0].run_bat}({self.current_batting_list[0].ball_used})', end='\t')
        print(f'{self.current_batting_list[1].player_name} - {self.current_batting_list[1].run_bat}({self.current_batting_list[1].ball_used})')
        print(f'{batting_team.team_name[:3].upper()} | {self.total_run} - {self.total_wicket}')
        print(f'Overs: {self.total_over}.{self.current_ball}')
        if self.current_bowler is not None:
            print(f'{self.current_bowler} - {self.current_bowler.run_ball}/{self.current_bowler.wicket_taken}')
    
    def set_bowler(self, bowler):
        self.current_bowler = bowler
        # print(self.current_bowler)

    def bowl(self, status):
        self.total_run += status
        self.striker.run_bat += status
        self.striker.ball_used += 1
        self.current_bowler.run_ball += status
        self.current_bowler.balls_bowled += 1
        self.current_ball += 1



# tournament
world_cup = T2Cup()

# teams
bangladesh = Team('Bangladesh')
india = Team('India')

# players
tamim = Player('Tamim Iqbal', bangladesh)
sakib = Player('Sakib Al Hasan', bangladesh)
mustafiz = Player('Mustafizur Rahman', bangladesh)

kohli = Player('Virat Kohli', india)
rohit = Player('Rohit Sharma', india)
bumra = Player('Bumra', india)


while True:
    print('Select team to be played')
    for i, team in enumerate(world_cup.all_teams):
        print(f'{i+1}. {team.team_name}')
    team_one_index, team_two_index = map(int, input('Enter Two Team Index: ').split(' '))
    team_one_index -= 1
    team_two_index -= 1
    team_one = world_cup.all_teams[team_one_index]
    team_two = world_cup.all_teams[team_two_index]
    toss_win = random.choice([team_one_index, team_two_index])
    if toss_win == team_one_index:
        toss_lose = team_two_index
    else:
        toss_lose = team_one_index
    toss_decision = random.choice(['bat', 'ball'])
    if toss_decision == 'bat':
        print(f'{world_cup.all_teams[toss_win]} win the toss and opt to {toss_decision} first')
        batting_team = world_cup.all_teams[toss_win]
        balling_team = world_cup.all_teams[toss_lose]
    else:
        print(f'{world_cup.all_teams[toss_win]} win the toss and opt to {toss_decision} first')
        batting_team = world_cup.all_teams[toss_lose]
        balling_team = world_cup.all_teams[toss_win]
    
    first_innings = Innings(team_one, team_two, batting_team, balling_team)
    first_innings.show_score_board()
    print('Choose bowler: ')
    for i, player in enumerate(balling_team.players_list_obj):
        print(f'{i+1}. {player.player_name}')
    bowler_index = int(input('Enter bowler index: '))
    bowler_index -= 1
    bowler = balling_team.players_list_obj[bowler_index]
    first_innings.set_bowler(bowler)
    print('\n')
    first_innings.bowl(6)
    first_innings.show_score_board()
    break