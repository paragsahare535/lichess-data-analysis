# Define a function to process the .pgn file
def analyze_games(file_path):
    tournament_games = 0
    non_tournament_games = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith("[Event"):
                event = line.split('"')[1]
                if 'tournament' in event.lower():
                    tournament_games += 1
                else:
                    non_tournament_games += 1

    return tournament_games, non_tournament_games

# Path to your .pgn file
file_path = r'C:\lichess_db_standard_rated_2016-12.pgn'

# Analyze the file
tournament_games, non_tournament_games = analyze_games(file_path)

# Print results
print(f'Tournament Games: {tournament_games}')
print(f'Non-Tournament Games: {non_tournament_games}')
