from flask import Blueprint, Flask, render_template, redirect, request

import repositories.bucket_list_repository as bucket_list_repository
import repositories.country_repository as country_repository
import repositories.destination_repository as destination_repository

from models.bucket_list import BucketList
from models.destination import Destination
from models.country import Country

country_blueprint = Blueprint("country", __name__)

@country_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

@country_blueprint.route("/countries/new", methods = ['GET'])
def new_country():
    return render_template("countries/new.html")

@country_blueprint.route("/countries", methods = ['POST'])
def create_country():
    country_name = request.form["country_name"]
    continent = request.form["continent"]
    country = Country(country_name, continent)
    country_repository.save(country)
    return redirect('/countries')





