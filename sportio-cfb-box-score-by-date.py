import pandas as pd
import http.client
import json
from twilio.rest import Client
import json

# 9H58rynABJvYqWXVKEYxlj9cCHzBWRG7daeKxtue

# Define the path to your JSON file
json_file_path = r"C:\temp\Github\sport-sms\key.json"

# Read the JSON file containing partial team names and week number
with open(json_file_path, "r") as json_file:
    keys = json.load(json_file)

api_key = '257077aa8bbe453ab5270f8a471be129'
date = '2023-09-09'
account_sid = keys["account_sid"]
auth_token = keys["auth_token"]
client = Client(account_sid, auth_token)

# Function to make HTTP request to the sports data API
def get_sports_data(api_key, date):
    conn = http.client.HTTPSConnection("api.sportsdata.io")
    payload = ''
    headers = {}
    conn.request("GET", f"/v3/cfb/stats/json/BoxScoresByDate/{date}?key={api_key}", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return json.loads(data)

# Get game data from the sports data API
game_data = get_sports_data(api_key, date)

# Extract data using list comprehensions
columns_to_extract = [
    'GameID', 'Season', 'SeasonType', 'Week', 'Status', 'Day', 'DateTime', 'AwayTeam', 'HomeTeam',
    'AwayTeamID', 'HomeTeamID', 'AwayTeamName', 'HomeTeamName', 'AwayTeamScore', 'HomeTeamScore',
    'PointSpread', 'OverUnder', 'AwayTeamMoneyLine', 'HomeTeamMoneyLine', 'Updated', 'Created',
    'GlobalGameID', 'GlobalAwayTeamID', 'GlobalHomeTeamID', 'StadiumID', 'YardLine', 'YardLineTerritory',
    'Down', 'Distance', 'Possession', 'IsClosed', 'GameEndDateTime', 'Title', 'HomeRotationNumber',
    'AwayRotationNumber', 'Channel', 'NeutralVenue', 'AwayPointSpreadPayout', 'HomePointSpreadPayout',
    'OverPayout', 'UnderPayout', 'DateTimeUTC', 'Attendance', 'Stadium', 'Period', 'TimeRemainingMinutes',
    'TimeRemainingSeconds'
]

data = {column: [game['Game'][column] for game in game_data] for column in columns_to_extract}

# Create a DataFrame from the extracted data
game_df = pd.DataFrame(data)

# Select columns of interest
columns_to_select = [
    'GameID', 'Status', 'AwayTeamName', 'AwayTeamScore', 'HomeTeamName', 'HomeTeamScore',
    'Period', 'TimeRemainingMinutes', 'TimeRemainingSeconds'
]

selected_columns_df = game_df[columns_to_select]

# Convert the DataFrame to an array
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
    
# output_string=  ("-" * 40) + output_string + '\n'

# # Send SMS message
# message = client.messages.create(
#     body=output_string,
#     from_='+18443882749',
#     to='+19893131968'
# )

# print(message.sid)


# Set the maximum length for each message
max_message_length = 1500

# Initialize a list to store the chunks of the output string
output_chunks = []

# Split the output_string into chunks of max_message_length characters
for i in range(0, len(output_string), max_message_length):
    output_chunk = output_string[i:i + max_message_length]
    output_chunks.append(output_chunk)

# Send SMS messages for each chunk
for i, output_chunk in enumerate(output_chunks):
    message_body = f"Chunk {i + 1}:\n\n{output_chunk}"
    message = client.messages.create(
        body=message_body,
        from_='+18443882749',
        to='+19893131968'
    )

    print(f"Message {i + 1} sent. SID: {message.sid}")