import csv
import meteostat
from datetime import datetime
import pandas as pd
   
    #fields required
tavg = []
prcp = []
snow = []
wspd = []
week = []

df = pd.read_csv('trip.csv')
    #converting datetime to weekday or weekend
for row in df.values:
    trip_date = [0]
    date = datetime.fromisoformat(trip_date)
    if date.weekday()<5:
        week.append('weekday')
    else:
        week.append('weekend')

    loc = meteostat.Point(42.38, -71.10, 70)
    data = meteostat.Daily(loc, date, date)
    data = data.fetch()
    #adding records to fields
    for item in data.values:
        tavg.append(item[0])
        prcp.append(item[3])
        snow.append(item[4])
        wspd.append(item[6])
   
    #creating dataframe
df['average_temperature']=tavg
df['precipitation']=prcp
df['snow']=snow
df['wind_speed']=wspd
df['weekday/weekend']=week
    #changing 'NA' to '0'
df['snow'] = df['snow'].fillna(0)
    #creating a new csv file
df.to_csv('tripandweather.csv')