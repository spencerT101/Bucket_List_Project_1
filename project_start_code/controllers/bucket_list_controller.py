from flask import Flask, render_template, redirect, request
from flask import Blueprint

from repositories import bucket_list_repository
from repositories import country_repository
from repositories import destination_repository

bucket_lists_blueprint = Blueprint("bucket_lists", __name__)


@bucket_lists_blueprint.route("/")
def bucket_lists():
    bucket_lists = bucket_list_repository.select_all()
    return render_template(bucket_)





