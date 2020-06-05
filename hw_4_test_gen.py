import requests
import pandas as pd

def create_standard_teams_test():
    """
    >>> create_standard_teams()
    returns a (m, 12) DataFrame
    """
    resp_dict = requests.get("https://data.nba.net/prod/v2/2019/teams.json").json()
    teams_list = resp_dict['league']['standard']
    df = pd.DataFrame()
    for i in teams_list:
        small_df = pd.DataFrame([i])
        df = df.append(small_df)
    df = df.reset_index(drop=True)
    return df

def create_nba_teams_test():
    """
    >>> create_nba_teams()
    returns a (30, 12) DataFrame
    """
    resp_dict = requests.get("https://data.nba.net/prod/v2/2019/teams.json").json()
    teams_list = resp_dict['league']['standard']
    df = pd.DataFrame()
    for i in teams_list:
        if i['isNBAFranchise']:
            small_df = pd.DataFrame([i])
            df = df.append(small_df)
    df = df.reset_index(drop=True)
    return df

def create_standard_players_test():
    """
    >>> create_standard_players()
    returns a (m, 15) DataFrame
    """
    resp_dict = requests.get("https://data.nba.net/prod/v1/2019/players.json").json()
    players_list = resp_dict['league']['standard']
    players_list_dict = []
    for p in players_list:
        player_dict = {}
        for k, v in p.items():
            if isinstance(v, str) or isinstance(v, bool):
                player_dict[k] = v
        players_list_dict.append(player_dict)
    df = pd.DataFrame(players_list_dict)
    selected_df = df.drop(['temporaryDisplayName', 'nbaDebutYear', 'yearsPro', 'lastAffiliation', 'isallStar'], axis=1)
    return selected_df

def create_nba_players_test():
    """
    >>> create_nba_players()
    returns a (m, 15) DataFrame
    """
    resp_dict = requests.get("https://data.nba.net/prod/v1/2019/players.json").json()
    players_list = resp_dict['league']['standard']
    players_list_dict = []
    for p in players_list:
        player_dict = {}
        for k, v in p.items():
            if isinstance(v, str) or isinstance(v, bool):
                player_dict[k] = v
        players_list_dict.append(player_dict)
    df = pd.DataFrame(players_list_dict)
    filtered_df = df[(df['teamId'] != '') & (df['isActive'])]
    selected_df = filtered_df.drop(['temporaryDisplayName', 'nbaDebutYear', 'yearsPro', 'lastAffiliation', 'isallStar'], axis=1)
    selected_df = selected_df.reset_index(drop=True)
    return selected_df

def count_nba_player_nationalities_test():
    """
    >>> count_nba_player_nationalities()
    returns a (m, 2) DataFrame
    """
    resp_dict = requests.get("https://data.nba.net/prod/v1/2019/players.json").json()
    players_list = resp_dict['league']['standard']
    players_list_dict = []
    for p in players_list:
        player_dict = {}
        for k, v in p.items():
            if isinstance(v, str) or isinstance(v, bool):
                player_dict[k] = v
        players_list_dict.append(player_dict)
    df = pd.DataFrame(players_list_dict)
    filtered_df = df[(df['teamId'] != '') & (df['isActive'])]
    ser = filtered_df['country'].value_counts()
    df = pd.DataFrame(ser).reset_index()
    df.columns = ['country', 'player_counts']
    df = df.sort_values(['player_counts', 'country'], ascending=[False, True])
    df = df.reset_index(drop=True)
    return df