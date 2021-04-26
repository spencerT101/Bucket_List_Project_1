from flask import Blueprint, Flask, render_template, redirect, request

import repositories.bucket_list_repository as bucket_list_repository
import repositories.country_repository as country_repository
import repositories.destination_repository as destination_repository

from models.bucket_list import BucketList
from models.destination import Destination
from models.country import Country

destinations_blueprint = Blueprint("destinations", __name__)


@destinations_blueprint.route("/destinations")
def lists():
    destinations = bucket_list_repository.select_all()
    return render_template("destinations/index.html", all_destinations = destinations)


@destinations_blueprint.route("/destinations/new", methods = ['GET'])
def new_list():
    country = country_repository.select_all()
    destination = destination_repository.select_all()
    return render_template("destinations/new_destination.html", all_destinations = destination, all_countries = country)


@destinations_blueprint.route("/destinations", methods = ['POST'])
def create_list():
    destination_name = request.form["destination_id"]
    destination_id = destination_repository.select(destination_name)
    destination = BucketList(destination_id)
    bucket_list_repository.save(destination)
    return redirect('/destinations')



@destinations_blueprint.route("/destinations/<id>", methods = ['GET'])
def show_destination(id):
    bucket_list = bucket_list_repository.select(id)
    destination = destination_repository.select_all()
    return render_template("destinations/show_destination.html", bucket_list = bucket_list, destination = destination)

@destinations_blueprint.route("/destinations/<id>/edit_destination", methods = ['GET'])
def edit_destination(id):
    bucket_list = bucket_list_repository.select(id)
    destination = destination_repository.select_all()
    country = country_repository.select_all()
    return render_template("destinations/edit_destination.html", bucket_list = bucket_list, all_destinations = destination, country = country)

@destinations_blueprint.route("/destinations/<id>", methods = ['POST'])
def update_bucket_list(id):
    new_id = request.form["destination"]
    # visited = request.form["visited"]
    destination = destination_repository.select(new_id)
    bucket_list = BucketList(destination, id)
    bucket_list_repository.update(bucket_list)
    return redirect('/destinations')

@destinations_blueprint.route("/destinations/<id>/delete", methods = ['POST'])
def delete_list(id):
    bucket_list_repository.delete(id)
    return redirect('/destinations')


