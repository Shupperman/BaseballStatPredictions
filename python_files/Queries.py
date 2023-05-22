# Access database using terminal through command on next line
# sqlite3 /Users/jasonshupper/Documents/Sports_Stuff/BaseballFiles/Database/baseball.db

class Queries:
    """
     Holds all the possible queries needed in our database.
    """

    ######################################################
    ##                   Games TABLE                    ##
    ######################################################

    # Create the games table
    create_games_table = ("CREATE TABLE IF NOT EXISTS games( "
                          "id VARCHAR(255) PRIMARY KEY, "
                          "location VARCHAR(255) NOT NULL, "
                          "date DATE NOT NULL, "
                          "stadium VARCHAR(255) NOT NULL, "
                          "fav_team VARCHAR(255) NOT NULL, "
                          "bet_line VARCHAR(255) NOT NULL, "
                          "game_length VARCHAR(255) NOT NULL, "
                          "away_team VARCHAR(255) NOT NULL, "
                          "home_team VARCHAR(255) NOT NULL, "
                          "home_plate VARCHAR(255) NOT NULL, "
                          "first_base VARCHAR(255) NOT NULL, "
                          "second_base VARCHAR(255) NOT NULL, "
                          "third_base VARCHAR(255) NOT NULL);")

    # Insertion into the games table
    insert_into_games = ("INSERT INTO games "
                         "(id, location, date, stadium, fav_team, "
                         "bet_line, game_length, away_team, home_team, "
                         "home_plate, first_base, second_base, third_base) "
                         "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);")

    # Read everything from the games table
    read_from_games = "SELECT * FROM games"

    # Read data about a single game
    read_player_from_games = "SELECT * FROM games WHERE id = ?"

    ######################################################
    ##                  ANALYSIS table                  ##
    ######################################################

    # Create the analysis table
    create_analysis_table = ("CREATE TABLE IF NOT EXISTS analysis( "
                             "id VARCHAR(255) PRIMARY KEY, "
                             "date DATE NOT NULL, "
                             "location VARCHAR(255) NOT NULL, "
                             "stadium VARCHAR(255) NOT NULL, "
                             "away_team VARCHAR(255) NOT NULL, "
                             "home_team VARCHAR(255) NOT NULL, "
                             "away_p VARCHAR(255) NOT NULL, "
                             "home_p VARCHAR(255) NOT NULL, "
                             "home_plate VARCHAR(255) NOT NULL, "
                             "first_base VARCHAR(255) NOT NULL, "
                             "second_base VARCHAR(255) NOT NULL, "
                             "third_base VARCHAR(255) NOT NULL, "
                             "nrfi INT NOT NULL);")
    
    # Drop the analysis table
    drop_analysis_table = ("DROP TABLE IF EXISTS analysis;")

    # Insertion into the games table
    insert_into_analysis = ("INSERT INTO analysis "
                           "(id, date, location, stadium, away_team, "
                           "home_team, away_p, home_p, home_plate, "
                           "first_base, second_base, third_base, nrfi) "
                           "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);")

    # Read everything from the analysis table
    read_from_analysis = "SELECT * FROM analysis"

    # Read data from analysis
    read_player_from_analysis = "SELECT * FROM analysis WHERE id = ?"




    ######################################################
    ##                  TEAM_URLS TABLE                 ##
    ######################################################

    # Create the team_urls table
    create_team_urls_table = ("CREATE TABLE IF NOT EXISTS team_urls( "
                              "id INT PRIMARY KEY AUTOINCREMENT,"
                              "team_name VARCHAR(50) NOT NULL,"
                              "url VARCHAR(100) NOT NULL)")

    # Insertion into the team_urls table
    insert_into_team_urls = ("INSERT INTO team_urls"
                             "(team_name, url) "
                             "VALUES (?, ?)")

    # Read everything from the team_urls table
    read_from_team_urls = "SELECT * FROM team_urls"

    ######################################################
    ##                   TEAMS TABLE                    ##
    ######################################################

    # Create the teams table
    create_teams_table = ("CREATE TABLE IF NOT EXISTS teams( "
                          "id INT PRIMARY KEY AUTOINCREMENT,"
                          "name VARCHAR(50) NOT NULL,"
                          "conference VARCHAR(30) NOT NULL,"
                          "division VARCHAR(30) NOT NULL,"
                          "location VARCHAR(100) NOT NULL,"
                          "head_coach VARCHAR(30) NOT NULL,"
                          "home_arena VARCHAR(40) NOT NULL)")

    # Insertion into the teams table
    insert_into_teams = ("INSERT INTO teams "
                         "(name, conference, division, location, head_coach, home_arena)"
                         "VALUES (?, ?, ?, ?, ?, ?)")

    # Read everything from the teams table
    read_from_teams = "SELECT * FROM teams"

    ######################################################
    ##                    URLS TABLE                    ##
    ######################################################

    # Create the urls table
    create_urls_table = ("CREATE TABLE IF NOT EXISTS urls( "
                         "id INT PRIMARY KEY AUTOINCREMENT,"
                         "name VARCHAR(50) NOT NULL,"
                         "url VARCHAR(100) NOT NULL)")

    # Insertion into the urls table
    insert_into_urls = ("INSERT INTO urls "
                        "(name, url)"
                        "VALUES (?, ?)")

    # Read everything from the urls table
    read_from_urls = "SELECT * FROM urls"
