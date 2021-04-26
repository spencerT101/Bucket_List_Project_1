import pdb

from models.bucket_list import BucketList
from models.country import Country
from models.destination import Destination

import repositories.destination_repository as destination_repository
import repositories.bucket_list_repository as bucket_list_repository

from repositories import country_repository 


destination_repository.delete_all()
country_repository.delete_all()
bucket_list_repository.delete_all()


country_1 = Country("France","Europe")
country_repository.save(country_1)

country_2 = Country("Republic of Korea", "Asia")
country_repository.save(country_2)

destination_1 = Destination("Paris",country_1)
destination_repository.save(destination_1)

destination_2 = Destination("Seoul", country_2)
destination_repository.save(destination_2)

destination_3  = Destination("Lille", country_1)
destination_repository.save(destination_3)

bucket_list_1 = BucketList(destination_1)
bucket_list_repository.save(bucket_list_1)

bucket_list_2 = BucketList(destination_2)
bucket_list_repository.save(bucket_list_2)






pdb.set_trace()
