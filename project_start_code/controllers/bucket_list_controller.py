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




