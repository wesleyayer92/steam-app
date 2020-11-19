import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import db

sql = ("SELECT Game.name, Playtime.playtime_forever, Playtime.playtime_2weeks "
        "FROM Playtime JOIN Game ON Game.appid=Playtime.appid "
        f"WHERE steamid={db.search_id};")
        
df = pd.read_sql_query(sql, db.conn)
pd.set_option('display.max_rows', df.shape[0]) # display all df rows
df.set_index('name', inplace=True)

# set time to hours instead of mins
df['playtime_forever'] = round(df['playtime_forever'] / 60, 2)
df['playtime_2weeks'] = round(df['playtime_2weeks'] / 60, 2)

df.sort_values(['playtime_2weeks', 'playtime_forever'], ascending=False, inplace=True)
print(df)
