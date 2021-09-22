# Perform unit testing for the api's in app.py


def UnitTest():
    # Perform unit testing for the api's in app.py

    def nflTeamsTest():

        #validate yaml
        from app import nflTeams
        assert nflTeams.get_team_names() == ['ARI', 
        'ATL', 
        'BAL', 
        'BUF', 
        'CAR', 
        'CHI', 
        'CIN', 
        'CLE', 
        'DAL', 
        'DEN', 
        'DET', 
        'GB', 
        'HOU', 
        'IND', 
        'JAX', 
        'KC', 
        'LAC', 
        'LAR', 
        'MIA', 
        'MIN', 
        'NE', 
        'NO', 
        'NYG', 
        'NYJ', 
        'OAK', 
        'PHI', 
        'PIT', 
        'SEA', 
        'SF', 
        'TB', 
        'TEN', 
        'WAS']

        #validate json
        from app import nflTeams
        assert nflTeams.get_team_names_json() == [{'team': 'ARI'},
        {'team': 'ATL'},
        {'team': 'BAL'},
        {'team': 'BUF'},
        {'team': 'CAR'},
        {'team': 'CHI'},
        {'team': 'CIN'},
        {'team': 'CLE'},
        {'team': 'DAL'},
        {'team': 'DEN'},
        {'team': 'DET'},
        {'team': 'GB'},
        {'team': 'HOU'},
        {'team': 'IND'},
        {'team': 'JAX'},
        {'team': 'KC'},
        {'team': 'LAC'},
        {'team': 'LAR'},
        {'team': 'MIA'},
        {'team': 'MIN'},
        {'team': 'NE'},
        {'team': 'NO'},
        {'team': 'NYG'},
        {'team': 'NYJ'},
        {'team': 'OAK'},
        {'team': 'PHI'},
        {'team': 'PIT'},
        {'team': 'SEA'},
        {'team': 'SF'},
        {'team': 'TB'},
        {'team': 'TEN'},
        {'team': 'WAS'}]

        #vaidate return type
        from app import nflTeams
        assert type(nflTeams.get_team_names()) == list
        assert type(nflTeams.get_team_names_json()) == list

UnitTest()




    

