import pandas as pd
import numpy as np
import random
import time
from io import StringIO #handle string from request
import cloudscraper

scraper = cloudscraper.create_scraper()  # crea sessione che bypassa Cloudflare
scraper.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
})

teams = [
    'ATL', 'BOS', 'BRK', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW',
    'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK',
    'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS',
]

team_dict = {
    'ATL': 'Hawks',
    'BOS': 'Celtics',
    'BRK': 'Nets',
    'CHO': 'Hornets',
    'CHI': 'Bulls',
    'CLE': 'Cavaliers',
    'DAL': 'Mavericks',
    'DEN': 'Nuggets',
    'DET': 'Pistons',
    'GSW': 'Warriors',
    'HOU': 'Rockets',
    'IND': 'Pacers',
    'LAC': 'Clippers',
    'LAL': 'Lakers',
    'MEM': 'Grizzlies',
    'MIA': 'Heat',
    'MIL': 'Bucks',
    'MIN': 'Timberwolves',
    'NOP': 'Pelicans',
    'NYK': 'Knicks',
    'OKC': 'Thunder',
    'ORL': 'Magic',
    'PHI': '76ers',
    'PHO': 'Suns',
    'POR': 'Trail Blazers',
    'SAC': 'Kings',
    'SAS': 'Spurs',
    'TOR': 'Raptors',
    'UTA': 'Jazz',
    'WAS': 'Wizards',
}

seasons = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']

nba_df = pd.DataFrame() #empty dataframe

#populate dataframe

for team in teams:
    for season in seasons:
        url = 'https://www.basketball-reference.com/teams/' + team + '/' + season + '/gamelog-advanced/'
        print(url)

        #get response
        res = scraper.get(url)

        # se Cloudflare o simili mostrano "Just a moment..." o il JS challenge, salva e salta
        if 'Just a moment' in res.text or 'cf_chl_opt' in res.text or res.status_code in (403, 429):
            print(f"Blocked by Cloudflare or rate-limited for {url} (status {res.status_code}) — saved debug and skipping")
            with open(f"debug_blocked_{team}_{season}.html", "w", encoding="utf-8") as f:
                f.write(res.text)
            # aspettare più a lungo prima di continuare (opzionale)
            time.sleep(30)
            continue

        #remove tag to unhide playoff table
        visible_res = res.text.replace('<!--', '').replace('-->', '')
        #visible_res = visible_res.replace('-->', '')

        #get dataframes
        try:
            df_list = pd.read_html(StringIO(visible_res), header=1)
        except:
            print(f"No tables found in {url} — salvo HTML per ispezione e salto")
            with open(f"debug_{team}_{season}.html", "w", encoding="utf-8") as f:
                f.write(visible_res)
            continue

        if (len(df_list)==1): #only regular season
            team_df = df_list[0]
        else:
            df_list[1]['Gtm'] = df_list[1]['Gtm'] + 82 #start counting from regular season
            team_df = pd.concat([df_list[0], df_list[1]], ignore_index=True) #concatenate regular season and playoff
        
        #little preprocess
        team_df = team_df.rename(columns={'Unnamed: 3':'At'})
        team_df['Win'] = team_df['Rslt'].apply(lambda x: 1 if x=='W' else 0)
        team_df.drop(columns=['Rslt'], inplace=True)
        
        #drop NaN or Gtm columns equal to 'Gtm'
        team_df = team_df.dropna(subset=['Gtm'])
        team_df = team_df[team_df['Gtm']!='Gtm']
        team_df.reset_index(drop=True, inplace=True) #reset indexes in order, after eliminating some rows, drop=True eliminates the old index column

        #keep useful columns

        #add some columns
        team_df['Team'] = team
        team_df['Season'] = season

        #append current team and season to nba_df
        nba_df = pd.concat([nba_df, team_df], ignore_index=True)
        nba_df.to_csv(f'./src/data/data.csv', index=False)

        #pause script to avoid restrictions by basketball-reference.com
        time.sleep(random.randint(4, 6))

print(nba_df)

        