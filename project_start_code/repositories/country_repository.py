from db.run_sql import run_sql

from models.bucket_list import BucketList
from models.country import Country
from models.destination import Destination

def save(country):
    sql = "INSERT INTO countries (name, continent) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.continent]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


def select_all():

#select all the countries in the database
#create a countries list
# Set the sql command to select all values from countries table and store in sql variable.
# run the sql function and store in variable called 'results'
#create a FOR loop to get country data and store in the countries list.
# Call the country class to take the row 'name', the row 'continent' and row 'id' and store in country variable.
#append these values in the countries list.
# return the list of all countries.

    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    
    for row in results:
        country = Country(row["name"], row["continent"], row["id"])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['continent'], result['id'])
    return country
    

def delete_all():
    sql  = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    

def update(country):
    sql = "UPDATE countries SET (name, continent) = (%s, %s) WHERE id = %s"
    values = [country.name, country.continent, country.id]
    run_sql(sql, values)
    



