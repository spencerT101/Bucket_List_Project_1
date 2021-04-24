import pdb

from models.bucket_list import Bucket_list
from models.country import Country
from models.destination import Destination


import repositories.bucket_list_repository as bucket_list
import repositories.destination_repository as destination_repository

from repositories import country_repository 

bucket_list_repository.delete_all()
destination_repository.delete_all()
country_repository.delete_all()


country_1 = Country("France","Europe")
country_repository.save(country_1)

country_2 = Country("Republic of Korea", "Asia")
country_repository.save(country_2)

destination_1 = Destination("Paris",country_1)
destination_repository.save(destination_1)

destination_2 = Destination("Seoul", country_2)
destination_repository.save(destination_2)
















pdb.set_trace()
