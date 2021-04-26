from db.run_sql import run_sql

from models.bucket_list import BucketList
from models.country import Country
from models.destination import Destination
import repositories.country_repository as country_repository


def save(destination):
    sql = "INSERT INTO destinations (city_name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [destination.city_name, destination.country.id, destination.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    destination.id = id
    return destination




def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        destination = Destination(result['city_name'], country, result['visited'], result['id'])
    return destination



def select_all():
    destinations = []
    sql = "SELECT * FROM destinations"
    results = run_sql(sql)
    
    for row in results:
        country = country_repository.select(row['country_id'])
        destination = Destination(row["city_name"],country, row["visited"], row["id"])
        destinations.append(destination)
    return destinations



def delete_all():
    sql  = "DELETE FROM destinations"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM destinations WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    

def update(destination):
    sql = "UPDATE destinations SET (city_name, country_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [destination.city_name, destination.country.id, destination.visited]
    run_sql(sql, values)
    
