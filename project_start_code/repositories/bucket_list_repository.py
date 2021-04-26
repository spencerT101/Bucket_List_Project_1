from db.run_sql import run_sql

from models.bucket_list import BucketList
from models.country import Country
from models.destination import Destination

import repositories.destination_repository as destination_repository


def save(bucket_list):
    sql = "INSERT INTO bucket_lists (destination_id) VALUES (%s) RETURNING *"
    values = [bucket_list.destination.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    bucket_list.id = id
    return bucket_list




def select(id):
    bucket_list = None
    sql = "SELECT * FROM bucket_lists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        destination = destination_repository.select(result['destination_id'])
        bucket_list = BucketList(destination, result['id'])
    return bucket_list



def select_all():
    bucket_lists = []

    sql = "SELECT * FROM bucket_lists"
    results = run_sql(sql)

    for row in results:
        destination = destination_repository.select(row['destination_id'])
        bucket_list = BucketList(destination, row['id'])
        bucket_lists.append(bucket_list)
    return bucket_lists



def delete_all():
    sql  = "DELETE FROM bucket_lists"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bucket_lists WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    

def update(bucket_list):
    sql = "UPDATE bucket_lists SET (destination_id) = (%s) WHERE id = %s"
    values = [bucket_list.destination.id, bucket_list.id]
    run_sql(sql, values)
    
