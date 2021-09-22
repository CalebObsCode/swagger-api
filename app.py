# Call dependencies
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, jsonify, render_template, send_from_directory
from marshmallow import Schema, fields
from yaml import load, dump
import requests
import os



# Instialize flask
app = Flask(__name__, template_folder='swagger/templates')


# Add routes
@app.route('/')
def index():
    return 'Sport API Development'


# Setup swagger
swagger_spec = APISpec(
    title='API DEV',
    version='1.0.0',
    openapi_version='3.0.2',
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)


class allSportsSchema():
    class Meta:
        fields = (
            'active',
            'details',
            'group',
            'has_outrights',
            'key',
            'title',
        )

    active = fields.Boolean()
    details = fields.String()
    group = fields.String()
    has_outrights = fields.Boolean()
    key = fields.String()
    title = fields.String()


class nflTeamsSchema():
    class Meta:
        fields = ('team_id',
                  'name',
                  'abbr',
                  'city',
                  'conference',
                  'division',
                  'logo_url',
                  'color',
                  'draft_pick',
                  'draft_round',
                  'draft_team',
                  'draft_pick_overall',
                  'draft_pick_round',
                  'draft_pick_position',
                  'draft_team_name',
                  'draft_team_abbr', 'draft_team_city',
                  'draft_team_conference',
                  'draft_team_division',
                  'draft_team_logo_url',
                  'draft_team_color',
                  'draft_team_draft_pick',
                  'draft_team_draft_round',
                  'draft_team_draft_team',
                  'draft_team_draft_pick_overall',
                  'draft_team_draft_pick_round',
                  'draft_team_draft_pick_position',
                  'draft_team_draft_team_name',
                  'draft_team_draft_team_abbr',
                  'draft_team_draft_team_city',
                  'draft_team_draft_team_conference',
                  'draft_team_draft_team_division',
                  )

    id = fields.Integer()
    name = fields.String()
    abbr = fields.String()
    city = fields.String()
    conference = fields.String()
    division = fields.String()
    logo_url = fields.String()
    color = fields.String()
    draft_pick = fields.Integer()
    draft_round = fields.Integer()
    draft_team = fields.Integer()
    draft_pick_overall = fields.Integer()
    draft_pick_round = fields.Integer()
    draft_pick_position = fields.Integer()
    draft_team_name = fields.String()
    draft_team_abbr = fields.String()
    draft_team_city = fields.String()
    draft_team_conference = fields.String()
    draft_team_division = fields.String()


class nflPlayersSchema():
    class Meta:
        fields = ('player_id',
                  'first_name',
                  'last_name',
                  'position',
                  'team',
                  'team_abbr',
                  'team_city',
                  'team_conference',
                  'team_division',
                  'team_logo_url',
                  'team_color',
                  'team_draft_pick',
                  'team_draft_round',
                  'team_draft_team',
                  'team_draft_pick_overall',
                  'team_draft_pick_round',
                  'team_draft_pick_position',
                  'team_draft_team_name',
                  'team_draft_team_abbr',
                  'team_draft_team_city',
                  'team_draft_team_conference',
                  'team_draft_team_division',
                  'team_draft_team_logo_url',
                  'team_draft_team_color',
                  'team_draft_team_draft_pick',
                  'team_draft_team_draft_round',
                  'team_draft_team_draft_team',
                  'team_draft_team_draft_pick_overall',
                  'team_draft_team_draft_pick_round',
                  'team_draft_team_draft_pick_position',
                  'team_draft_team_draft_team_name',
                  'team_draft_team_draft_team_abbr',
                  'team_draft_team_draft_team_city',
                  'team_draft_team_draft_team_conference',
                  'team_draft_team_draft_team_division',
                  'team_draft_team_draft_team_logo_url',
                  'team_draft_team_draft_team_color',
                  'team_draft_team_draft_team_draft_pick',
                  'team_draft_team_draft_team_draft_round',
                  'team_draft_team_draft_team_draft_team',
                  'team_draft_team_draft_team_draft_pick_overall',
                )

    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    position = fields.String()
    team = fields.String()
    team_abbr = fields.String()
    team_city = fields.String()
    team_conference = fields.String()
    team_division = fields.String()
    team_logo_url = fields.String()
    team_color = fields.String()
    team_draft_pick = fields.Integer()
    team_draft_round = fields.Integer()
    team_draft_team = fields.Integer()
    team_draft_pick_overall = fields.Integer()
    team_draft_pick_round = fields.Integer()
    team_draft_pick_position = fields.Integer()
    team_draft_team_name = fields.String()
    team_draft_team_abbr = fields.String()
    team_draft_team_city = fields.String()
    team_draft_team_conference = fields.String()
    team_draft_team_division = fields.String()
    team_draft_team_logo_url = fields.String()
    team_draft_team_color = fields.String()
    team_draft_team_draft_pick = fields.Integer()
    team_draft_team_draft_round = fields.Integer()
    team_draft_team_draft_team = fields.Integer()
    team_draft_team_draft_pick_overall = fields.Integer()

class nflScheduleSchema():
    class Meta:
        fields = ('game_id',
                  'game_date',
                  'game_time',
                  'game_time_zone',
                  'game_week',
                  'game_season',
                  'game_season_type',
                  'game_week_type',
                  'game_type',
                  'game_location',
                  'game_home_team',
                  'game_home_team_abbr',
                  'game_home_team_city',
                  'game_home_team_conference',
                  'game_home_team_division',
                  'game_home_team_logo_url',
                  'game_home_team_color',
                  
            'game_away_team',
            'game_away_team_abbr',
            'game_away_team_city',
            'game_away_team_conference',
            'game_away_team_division',
            'game_away_team_logo_url',
            'game_away_team_color',
            
        )

    id = fields.Integer()
    game_date = fields.String()
    game_time = fields.String()
    game_time_zone = fields.String()
    game_week = fields.Integer()
    game_season = fields.Integer()
    game_season_type = fields.String()
    game_week_type = fields.String()
    game_type = fields.String()
    game_location = fields.String()
    game_home_team = fields.String()
    game_home_team_abbr = fields.String()
    game_home_team_city = fields.String()
    game_home_team_conference = fields.String()
    game_home_team_division = fields.String()
    game_home_team_logo_url = fields.String()
    game_home_team_color = fields.String()
    game_away_team = fields.String()
    game_away_team_abbr = fields.String()
    game_away_team_city = fields.String()
    game_away_team_conference = fields.String()
    game_away_team_division = fields.String()
    game_away_team_logo_url = fields.String()
    game_away_team_color = fields.String()


class nflPlayersResponseSchema():
    class Meta:
        fields = ('response', 'data')

    response = fields.String()
    data = fields.List(fields.Nested(nflPlayersSchema))

class nflResonseSchema():
    class Meta:
        fields = ('response', 'data')

    response = fields.String()
    data = fields.List(fields.Nested(nflTeamsSchema))

class allSportsResonseSchema():
    class Meta:
        fields = ('response', 'data')

    response = fields.String()
    data = fields.List(fields.Nested(allSportsSchema))


# Add routes for allSports
@app.route('/allSports')
def allSports():
    # Get data from API
    # Return dummy data for now
    """ Get list of all sports
        ---
        get:
            description: Get list of all Sports
            responses:
                '200':
                    description: Successful
                '400':
                    description: Bad Request
                '500':
                    description: Internal Server Error
    """
    # Get list of nfl teams
    url = "https://odds.p.rapidapi.com/v1/sports"

    RAPID_API_HOST = os.environ.get('x-rapidapi-host')
    RAPID_API_KEY = os.environ.get('x-rapidapi-key')

    headers = {
    'x-rapidapi-host': os.environ.get(RAPID_API_HOST),
    'x-rapidapi-key' : os.environ.get(RAPID_API_KEY)
    }

    response = requests.request("GET", url, headers=headers)

    # Return data
    return jsonify(response.json())


with app.test_request_context():
    swagger_spec.path(view=allSports)

# Add routes
@app.route('/nflTeams')
def nflTeams():
    # Get data from API
    # Return dummy data for now
    # Todo: Add real data
    """ Get List of nfl teams
       ---
       get:
            description: Get list of nfl teams
            responses:
                '200':
                    description: Successful
                '400':
                    description: Bad Request
                '500':
                    description: Internal Server Error
    """


    # Get list of nfl teams
    url = "https://therundown-therundown-v1.p.rapidapi.com/sports/2/teams"

    RAPID_API_HOST = os.environ.get('x-rapidapi-host')
    RAPID_API_KEY = os.environ.get('x-rapidapi-key')

    headers = {
    'x-rapidapi-host': os.environ.get(RAPID_API_HOST),
    'x-rapidapi-key' : os.environ.get(RAPID_API_KEY)
    }

    response = requests.request("GET", url, headers=headers)

    # Return data
    return jsonify(response.json())


with app.test_request_context():
    swagger_spec.path(view=nflTeams)




# Add routes to get informaion about a specific team
@app.route('/nflTeams/<int:team_id>')
def nflTeam(team_id):
    # Get data from API
    # Return dummy data for now
    """ Get individual nfl team
        ---
        get:
            description: Get information about a specific nfl team
            parameters:
              - in: path
                name: team_id
                schema:
                    type: integer
                required: true
                description: The id of the nfl team
            responses:
                '200':
                    description: Successful
                '400':
                    description: Bad Request
                '500':
                    description: Internal Server Error
    """

    data = {
        'team_id': 1,
        'name': 'Arizona Cardinals',
        'abbr': 'ARI',
        'city': 'Phoenix',
        'conference': 'NFC',
        'division': 'West',
        'logo_url': 'https://s3.amazonaws.com/nfl-assets/img/gbl-ico-team/HOU/HOU.png',
        'color': '#A71930',
        'draft_pick': 1,
        'draft_round': 1,
        'draft_team': 1,
        'draft_pick_overall': 1,
        'draft_pick_round': 1,
        'draft_pick_position': 1,
        'draft_team_name': 'Arizona Cardinals',
        'draft_team_abbr': 'ARI',
        'draft_team_city': 'Phoenix',
        'draft_team_conference': 'NFC',
        'draft_team_division': 'West',

    }

    #validate parameters
    if team_id != data['team_id']:
        return jsonify({'error': 'Invalid team_id'}), 400

    # validate query parameters
    if request.args.get('team_id') != data['team_id']:
        return jsonify({'error': 'Invalid team_id'}), 400

    # Handle invalid query parameters
    if request.args.get('team_id') is None:
        return jsonify({'error': 'Invalid team_id'}), 400

    # Handle empty query parameters
    if request.args.get('team_id') == '':
        return jsonify({'error': 'Invalid team_id'}), 400
    
    # 
    

    # Return data
    return jsonify(data)

with app.test_request_context():
    swagger_spec.path(view=nflTeam)


# Add routes to get informaion about a specific players using first and last name. First name is required. Last name is optional.
@app.route('/nflPlayers/<string:first_name>/<string:last_name>')
def nflPlayer(first_name, last_name):
    # Get data from API
    # Return dummy data for now
    """ Get individual nfl player
        ---
        get:
            description: Get Information about a specific nfl player
            parameters:
              - in: path
                name: first_name
                schema:
                    type: string
                required: true
                description: The first name of the nfl player
              - in: path
                name: last_name
                schema:
                    type: string
                required: optional
                description: The last name of the nfl player
            responses:
                '200':
                    description: Successful
                '400':
                    description: Bad Request
                '500':
                    description: Internal Server Error
    """

    data = [{
        'first_name': 'Alex',
        'last_name': 'Smith',
        'team_id': 1,
        'team_name': 'Arizona Cardinals',
        'team_abbr': 'ARI',
        'team_city': 'Phoenix',
        'team_conference': 'NFC',
        'team_division': 'West',
        'position': 'QB',
        'position_type': 'Quarterback',
        'position_category': 'Offensive',
        'position_sub_category': 'Wide Receiver',
    },

    {
        'first_name': 'Tom',
        'last_name': 'Brady',
        'team_id': 2,
        'team_name': 'Tampa Bay Buccaneers',
        'team_abbr': 'TB',
        'team_city': 'Tampa',
        'team_conference': 'NFC',
        'team_division': 'South',
        'position': 'QB',
        'position_type': 'Quarterback',
        'position_category': 'Offensive',
        'position_sub_category': 'Wide Receiver',
    },
    
    ]

    
    # Handle first name
    if first_name == '':
        return jsonify({'error': 'Invalid first_name'}), 400

    # Handle last name
    if last_name == '':
        last_name = None

    # Filter data
    data = list(filter(lambda x: x['first_name'] == first_name and x['last_name'] == last_name, data))

    # Handle no data
    if len(data) == 0:
        return jsonify({'error': 'No data found'}), 400

    # Handle duplicate data
    if len(data) > 1:
        return jsonify({'error': 'Duplicate data found'}), 400


    # Return data
    return jsonify(data)

with app.test_request_context():
    swagger_spec.path(view=nflPlayer)
    

# Add routes for display nfl schedule
@app.route('/nflSchedule')
def nflSchedule():
    # Get data from API
    # Return dummy data for now
    """ Get nfl schedule
        ---
        get:
            description: Get the nfl schedule
            responses:
                '200':
                    description: Successful
                '400':
                    description: Bad Request
                '500':
                    description: Internal Server Error
    """

    data = [{
        'game_id': 1,
        'week': 1,
        'season': 2019,
        'home_team_id': 1,
        'home_team_name': 'Arizona Cardinals',
        'home_team_abbr': 'ARI',
        'home_team_city': 'Phoenix',
        'home_team_conference': 'NFC',
        'home_team_division': 'West',
        'home_team_logo_url': 'https://s3.amazonaws.com/nfl-assets/img/gbl-ico-team/ARI/ARI.png',
        'away_team_id': 2,
        'away_team_name': 'Tampa Bay Buccaneers',
        'away_team_abbr': 'TB',
        'away_team_city': 'Tampa',
        'away_team_conference': 'NFC',
        'away_team_division': 'South',
        'away_team_logo_url': 'https://s3.amazonaws.com/nfl-assets/img/gbl-ico-team/TB/TB.png',
        'date': '2019-09-01',
        'time': '2019-09-01T01:00:00.000Z',
        'time_zone': 'America/New_York',
        'tv_network': 'FOX',
        'tv_station': 'FOX',
        'tv_station_url': 'http://www.fox.com/',
        'tv_station_id': 'FOX',
        'tv_station_name': 'FOX',
        'tv_station_logo_url': 'https://s3.amazonaws.com/nfl-assets/img/gbl-ico-team/FOX/FOX.png',
        'tv_station_logo_url_alt': 'https://s3.amazonaws.com/nfl-assets/img',
}]


# Add routes to display nfl schedule for a specific week
@app.route('/nflSchedule/<int:week>')
def nflScheduleWeek(week):
    # Get data from API
    # Return dummy data for now
    """ Get nfl schedule for a specific week
        ---
        get:
            description: Get the nfl schedule for a specific week
            parameters:
              - in: path
                name: week
                schema:
                    type: integer
                required: true
                description: The week of the nfl schedule
            responses:
                '200':
                    description: Successful
                '400':
                    description: Bad Request
                '500':
                    description: Internal Server Error
    """

    data = [{
        'game_id': 1,
        'week': 1,
        'season': 2019,
        'home_team_id': 1,
        'home_team_name': 'Arizona Cardinals',
        'home_team_abbr': 'ARI',
        'home_team_city': 'Phoenix',
        'home_team_conference': 'NFC',
        'home_team_division': 'West',
        'home_team_logo_url': 'https://s3.amazonaws.com/nfl-assets/img/gbl-ico-team/ARI/ARI.png',
        'away_team_id': 2,
        'away_team_name': 'Tampa Bay Buccaneers',
        'away_team_abbr': 'TB',
        'away_team_city': 'Tampa',
        'away_team_conference': 'NFC',
        'away_team_division': 'South',
        'away_team_logo_url': 'https://s3.amazonaws.com/nfl-assets/img/gbl-ico-team/TB/TB.png',
        'date': '2019-09-01',
        'time': '2019-09-01T01:00:00.000Z',
        'time_zone': 'America/New_York',
        'tv_network': 'FOX',
        'tv_station': 'FOX',
        'tv_station_url': 'http://www.fox.com/',
        'tv_station_id': 'FOX',
        'tv_station_name': 'FOX',

    }]

# Expose swagger json
@app.route('/api/swagger.json')
def get_swagger_json():
    return jsonify(swagger_spec.to_dict())

# define route for swagger-ui


@app.route('/docs')
@app.route('/docs/<path:path>')
def get_swagger_ui(path=None):
    if path is None or path == 'index.html':

        return render_template('index.html', base_url='/docs')
    else:
        return send_from_directory('./swagger/static', path)

#handle 500 error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



# main method
if __name__ == '__main__':
    app.run(debug=True)