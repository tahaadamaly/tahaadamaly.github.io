# This script is from pyErgast, a module that was created to access the Ergast F1 API and was not written by me. 
# I use this script in some cases to access the Ergast API given the multiple levels of nesting in the API and difficulty accessing it


import requests
import pandas as pd


def get_drivers(year=None, race=None):
    
    if year and race:
        url = 'http://ergast.com/api/f1/{}/drivers.json?limit=100000'.format(year, race)
    elif year:
        url = 'http://ergast.com/api/f1/{}/drivers.json?limit=100000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/drivers.json?limit=100000'
    r = requests.get(url)

    assert r.status_code == 200, 'Cannot connect to Ergast API'
    drivers = r.json()
    result = pd.DataFrame(drivers["MRData"]["DriverTable"]['Drivers'])

    return result


def get_constructors(year=None, race=None):
   
    if year and race:
        url = 'http://ergast.com/api/f1/{}/constructors.json?limit=100000'.format(year, race)
    elif year:
        url = 'http://ergast.com/api/f1/{}/constructors.json?limit=100000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/constructors.json?limit=100000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    constructors = r.json()
    result = pd.DataFrame(constructors["MRData"]["ConstructorTable"]['Constructors'])

    return result


def get_circuits(year=None, race=None):
    
    if year and race:
        url = 'http://ergast.com/api/f1/{}/circuits.json?limit=100000'.format(year, race)
    elif year:
        url = 'http://ergast.com/api/f1/{}/circuits.json?limit=100000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/circuits.json?limit=100000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    circuits = r.json()
    result = pd.DataFrame(circuits["MRData"]["CircuitTable"]["Circuits"])

    # Grabbing latitude, longtitude, locality and country separately
    geo = result['Location']
    latitude, longtitude, locality, country = ([] for i in range(4))
    for track in geo:
        latitude.append(track['lat'])
        longtitude.append(track['long'])
        locality.append(track['locality'])
        country.append(track['country'])
    result['Latitude'] = latitude
    result['Longtitude'] = longtitude
    result['Locality'] = locality
    result['Country'] = country
    result = result.drop('Location', axis=1)
    return result


def find_driverid(firstname, lastname):
    dfDrivers = get_drivers()
    result = dfDrivers[
        dfDrivers['driverId'].str.contains(firstname.lower()) | dfDrivers['driverId'].str.contains(lastname.lower())]
    return result


def find_constructorid(name):
    
    dfConstructors = get_constructors()
    result = dfConstructors[dfConstructors['constructorId'].str.contains(name.lower())]
    return result


def find_circuitid(circuit):
   
    dfCircuits = get_circuits()
    result = dfCircuits[dfCircuits['circuitId'].str.lower().str.contains(circuit.lower()) |
                        dfCircuits['circuitName'].str.lower().str.contains(circuit.lower()) |
                        dfCircuits['Locality'].str.lower().str.contains(circuit.lower()) |
                        dfCircuits['Country'].str.lower().str.contains(circuit.lower())]
    return result


def get_race_result(year=None, race=None):

    if year or race:
        assert year and race, 'You must specify both a year and a race'
        url = 'http://ergast.com/api/f1/{}/{}/results.json?limit=1000000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/current/last/results.json?limit=1000000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    race_result = r.json()
    result_dict = race_result["MRData"]['RaceTable']['Races'][0]['Results']

    # Unpack the lists of dicts in result_dict and reformat the result
    for driver in result_dict:
        drive_dict = unpack_lists(driver)
        driver_info = drive_dict[0]
        constructor_info = drive_dict[1]
        driver['driver'] = driver_info['givenName'] + ' ' + driver_info['familyName']
        driver['driverID'] = driver_info['driverId']
        driver['nationality'] = driver_info['nationality']
        driver['constructor'] = constructor_info['name']
        driver['constructorID'] = constructor_info['constructorId']

    # Select the columns that are relevant to the race result
    cols = ['number', 'position', 'positionText', 'grid', 'points', 'driverID', 'driver',
            'nationality', 'constructorID', 'constructor', 'laps', 'status', 'Time']
    return pd.DataFrame(result_dict)[cols]


def get_qualifying_result(year=None, race=None):
    
    if year and race:
        assert year >= 1996, 'Qualifying data only available starting from 1996'
        url = 'http://ergast.com/api/f1/{}/{}/qualifying.json?limit=1000000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/current/last/qualifying.json?limit=1000000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    race_result = r.json()
    result_dict = race_result["MRData"]['RaceTable']['Races'][0]['QualifyingResults']

    # Unpack the lists of dicts in result_dict and reformat the result
    for driver in result_dict:
        drive_dict = unpack_lists(driver)
        driver_info = drive_dict[0]
        constructor_info = drive_dict[1]
        driver['driver'] = driver_info['givenName'] + ' ' + driver_info['familyName']
        driver['driverID'] = driver_info['driverId']
        driver['nationality'] = driver_info['nationality']
        driver['constructor'] = constructor_info['name']
        driver['constructorID'] = constructor_info['constructorId']

    # Specify the columns to be returned, taking into account changing qualifying formats
    cols = ['number', 'position', 'driverID', 'driver', 'nationality', 'constructorID', 'constructor', 'Q1']
    if 'Q2' in result_dict[0].keys():
        cols.append('Q2')
    if 'Q3' in result_dict[0].keys():
        cols.append('Q3')
    return pd.DataFrame(result_dict)[cols]


def get_schedule(year=None):
    
    if year:
        url = 'http://ergast.com/api/f1/{}.json?limit=1000000'.format(year)
    else:
        url = 'http://ergast.com/api/f1/current.json?limit=1000000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    schedule = r.json()['MRData']['RaceTable']['Races']

    # Unpack the lists of dicts in result_dict and reformat the result
    for race in schedule:
        circuit = unpack_lists(race)[0]
        race['circuitID'] = circuit['circuitId']
        race['circuitName'] = circuit['circuitName']
        race['locality'] = circuit['Location']['locality']
        race['country'] = circuit['Location']['country']
        del race['Circuit']

    return pd.DataFrame(schedule)


def driver_standings(year=None, race=None):
    
    if year and race:
        url = 'http://ergast.com/api/f1/{}/{}/driverStandings.json?limit=1000000'.format(year, race)
    elif year:
        url = 'http://ergast.com/api/f1/{}/driverStandings.json?limit=1000000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/current/driverStandings.json?limit=1000000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    driverStandings = r.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

    for driver in driverStandings:
        driver['driverID'] = driver['Driver']['driverId']
        driver['driver'] = driver['Driver']['givenName'] + ' ' + driver['Driver']['familyName']
        driver['nationality'] = driver['Driver']['nationality']
        driver['constructorID'] = driver['Constructors'][0]['constructorId']
        driver['constructor'] = driver['Constructors'][0]['name']
        del driver['Driver']
        del driver['Constructors']

    return pd.DataFrame(driverStandings)


def constructor_standings(year=None, race=None):
   
    if year and race:
        assert year >= 1958, 'Constructor standings only available starting 1958'
        url = 'http://ergast.com/api/f1/{}/constructorStandings.json?limit=1000000'.format(year, race)
    elif year:
        assert year >= 1958, 'Constructor standings only available starting 1958'
        url = 'http://ergast.com/api/f1/{}/constructorStandings.json?limit=1000000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/current/constructorStandings.json?limit=1000000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    constructorStandings = r.json()['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    for constructor in constructorStandings:
        constructor['constructorID'] = constructor['Constructor']['constructorId']
        constructor['name'] = constructor['Constructor']['name']
        constructor['nationality'] = constructor['Constructor']['nationality']
        del constructor['Constructor']

    return pd.DataFrame(constructorStandings)


def query_driver(driverid):
   
    url = 'http://ergast.com/api/f1/drivers/{}/driverStandings.json?limit=1000000'.format(driverid)
    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    seasons = r.json()['MRData']['StandingsTable']['StandingsLists']

    # Extracting data from json
    for season in seasons:
        for key, value in season['DriverStandings'][0].items():
            season[key] = value
        season['driver'] = season['Driver']['givenName'] + ' ' + season['Driver']['familyName']
        season['nationality'] = season['Driver']['nationality']
        season['constructorID'] = season['Constructors'][0]['constructorId']
        season['constructor'] = season['Constructors'][0]['name']
        del season['DriverStandings']
        del season['Driver']
        del season['Constructors']

    return pd.DataFrame(seasons)


def query_constructor(constructorid):
    
    url = 'http://ergast.com/api/f1/constructors/{}/constructorStandings.json?limit=1000000'.format(constructorid)
    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    seasons = r.json()['MRData']['StandingsTable']['StandingsLists']

    # Extracting data from json
    for season in seasons:
        for key, value in season['ConstructorStandings'][0].items():
            season[key] = value
        season['constructorID'] = season['Constructor']['constructorId']
        season['constructor'] = season['Constructor']['name']
        season['nationality'] = season['Constructor']['nationality']
        del season['Constructor']
        del season['ConstructorStandings']

    return pd.DataFrame(seasons)


def unpack_lists(driver):
    
    result = []
    for key in driver.keys():
        if isinstance(driver[key], dict):
            result.append(driver[key])
    return result
