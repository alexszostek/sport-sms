import pandas as pd
import http.client
import json
import numpy as np
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACdc4a3abfabd69526d187529200b531de'
auth_token = '31e84398dcc6550acf59f6f7a8c8e09d'
client = Client(account_sid, auth_token)

conn = http.client.HTTPSConnection("api.sportsdata.io")
payload = ''
headers = {}
conn.request("GET", "/v3/cfb/stats/json/BoxScoresByDate/2023-09-01?key=257077aa8bbe453ab5270f8a471be129", payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")

game_data = json.loads(data)

# Assuming game_data holds the list of game dictionaries

# Create empty lists to store data for each column
game_ids = []
seasons = []
season_types = []
weeks = []
statuses = []
days = []
date_times = []
away_teams = []
home_teams = []
period = []
time_remaining_minutes = []
time_remaining_seconds = []
away_team_ids = []
home_team_ids = []
away_team_names = []
home_team_names = []
away_team_scores = []
home_team_scores = []
point_spreads = []
over_unders = []
away_team_money_lines = []
home_team_money_lines = []
updated_times = []
created_times = []
global_game_ids = []
global_away_team_ids = []
global_home_team_ids = []
stadium_ids = []
yard_lines = []
yard_line_territories = []
downs = []
distances = []
possessions = []
is_closed = []
game_end_date_times = []
titles = []
home_rotation_numbers = []
away_rotation_numbers = []
channels = []
neutral_venues = []
away_point_spread_payouts = []
home_point_spread_payouts = []
over_payouts = []
under_payouts = []
date_times_utc = []
attendances = []
stadiums = []

# Loop through each game and extract data for each column
for game in game_data:
    game_info = game['Game']
    game_ids.append(game_info['GameID'])
    seasons.append(game_info['Season'])
    season_types.append(game_info['SeasonType'])
    weeks.append(game_info['Week'])
    statuses.append(game_info['Status'])
    days.append(game_info['Day'])
    date_times.append(game_info['DateTime'])
    away_teams.append(game_info['AwayTeam'])
    home_teams.append(game_info['HomeTeam'])
    away_team_ids.append(game_info['AwayTeamID'])
    home_team_ids.append(game_info['HomeTeamID'])
    away_team_names.append(game_info['AwayTeamName'])
    home_team_names.append(game_info['HomeTeamName'])
    away_team_scores.append(game_info['AwayTeamScore'])
    home_team_scores.append(game_info['HomeTeamScore'])
    point_spreads.append(game_info['PointSpread'])
    over_unders.append(game_info['OverUnder'])
    away_team_money_lines.append(game_info['AwayTeamMoneyLine'])
    home_team_money_lines.append(game_info['HomeTeamMoneyLine'])
    updated_times.append(game_info['Updated'])
    created_times.append(game_info['Created'])
    global_game_ids.append(game_info['GlobalGameID'])
    global_away_team_ids.append(game_info['GlobalAwayTeamID'])
    global_home_team_ids.append(game_info['GlobalHomeTeamID'])
    stadium_ids.append(game_info['StadiumID'])
    yard_lines.append(game_info['YardLine'])
    yard_line_territories.append(game_info['YardLineTerritory'])
    downs.append(game_info['Down'])
    distances.append(game_info['Distance'])
    possessions.append(game_info['Possession'])
    is_closed.append(game_info['IsClosed'])
    game_end_date_times.append(game_info['GameEndDateTime'])
    titles.append(game_info['Title'])
    home_rotation_numbers.append(game_info['HomeRotationNumber'])
    away_rotation_numbers.append(game_info['AwayRotationNumber'])
    channels.append(game_info['Channel'])
    neutral_venues.append(game_info['NeutralVenue'])
    away_point_spread_payouts.append(game_info['AwayPointSpreadPayout'])
    home_point_spread_payouts.append(game_info['HomePointSpreadPayout'])
    over_payouts.append(game_info['OverPayout'])
    under_payouts.append(game_info['UnderPayout'])
    date_times_utc.append(game_info['DateTimeUTC'])
    attendances.append(game_info['Attendance'])
    stadiums.append(game_info['Stadium'])
    period.append(game_info['Period'])
    time_remaining_minutes.append(game_info['TimeRemainingMinutes'])
    time_remaining_seconds.append(game_info['TimeRemainingSeconds'])

# Create a dictionary to hold all the extracted data
data = {
    'GameID': game_ids,
    'Season': seasons,
    'SeasonType': season_types,
    'Week': weeks,
    'Status': statuses,
    'Day': days,
    'DateTime': date_times,
    'AwayTeam': away_teams,
    'HomeTeam': home_teams,
    'AwayTeamID': away_team_ids,
    'HomeTeamID': home_team_ids,
    'AwayTeamName': away_team_names,
    'HomeTeamName': home_team_names,
    'AwayTeamScore': away_team_scores,
    'HomeTeamScore': home_team_scores,
    'PointSpread': point_spreads,
    'OverUnder': over_unders,
    'AwayTeamMoneyLine': away_team_money_lines,
    'HomeTeamMoneyLine': home_team_money_lines,
    'Updated': updated_times,
    'Created': created_times,
    'GlobalGameID': global_game_ids,
    'GlobalAwayTeamID': global_away_team_ids,
    'GlobalHomeTeamID': global_home_team_ids,
    'StadiumID': stadium_ids,
    'YardLine': yard_lines,
    'YardLineTerritory': yard_line_territories,
    'Down': downs,
    'Distance': distances,
    'Possession': possessions,
    'IsClosed': is_closed,
    'GameEndDateTime': game_end_date_times,
    'Title': titles,
    'HomeRotationNumber': home_rotation_numbers,
    'AwayRotationNumber': away_rotation_numbers,
    'Channel': channels,
    'NeutralVenue': neutral_venues,
    'AwayPointSpreadPayout': away_point_spread_payouts,
    'HomePointSpreadPayout': home_point_spread_payouts,
    'OverPayout': over_payouts,
    'UnderPayout': under_payouts,
    'DateTimeUTC': date_times_utc,
    'Attendance': attendances,
    'Stadium': stadiums,
    'Period': period,
    'TimeRemainingMinutes': time_remaining_minutes,
    'TimeRemainingSeconds': time_remaining_seconds
}

# Create a DataFrame from the dictionary
game_df = pd.DataFrame(data)

# List of columns you want to select
columns_to_select = ['GameID','Status','AwayTeamName', 'AwayTeamScore', 'HomeTeamName', 'HomeTeamScore', 'Period', 'TimeRemainingMinutes', 'TimeRemainingSeconds']

# Create a new DataFrame with only the selected columns
selected_columns_df = game_df[columns_to_select]

# filtered_game_df = selected_columns_df[game_df['HomeTeamName'] == 'Michigan State Spartan']

# print(selected_columns_df)

games_array = selected_columns_df.values

# Initialize an empty string to store the output
output_string = ""

for games in games_array:
    hTeam = str(games[4])
    aTeam = str(games[2])
    aScore = str(games[3])
    hScore = str(games[5])
    period = str(games[6])
    clock = str(games[7]) + ':' + str(games[8])
    game_clock = 'Quarter ' + period + ' ' + clock
    output = hTeam + '\t' + hScore + '\n' + aTeam + '\t' + aScore + '\n' + game_clock + '\n' + ("-" * 20) + '\n'
    output_string = output_string + output
    
output_string=  ("-" * 40) + output_string + '\n'

message = client.messages.create(
    body= "\n\n" + output_string,  
    from_='+18443882749',
    to='+19893131968'
)

print(message.sid)
