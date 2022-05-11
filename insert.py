#! /usr/bin/env python
import csv
import pprint
import pymongo

if __name__ == '__main__':
    columns = ["country", "country_long", "name", "gppd_idnr", "capacity_mw", "latitude","longitude","primary_fuel","other_fuel1","other_fuel2","other_fuel3","commissioning_year","owner","source","url","geolocation_source","wepp_id","year_of_capacity_data","generation_gwh_2013","generation_gwh_2014","generation_gwh_2015","generation_gwh_2016","generation_gwh_2017","generation_gwh_2018","generation_gwh_2019","generation_data_source","estimated_generation_gwh_2013","estimated_generation_gwh_2014","estimated_generation_gwh_2015","estimated_generation_gwh_2016","estimated_generation_gwh_2017","estimated_generation_note_2013","estimated_generation_note_2014","estimated_generation_note_2015","estimated_generation_note_2016","estimated_generation_note_2017"]
    entries = []
    with open('global_power_plant_database.csv',"rt",encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader) # skip the first line
        for row in reader:
            entries.append(dict(zip(columns, row)))

    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['db']
    plants = db['plants']
    plants.insert_many(entries)

    for post in plants.find():
        pprint.pprint(post)