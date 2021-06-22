import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")
django.setup()

from faker import Faker
from appTwo.models import User


fakegen = Faker()

def populate(N=10):
	for entry in range(N):
		tmp_name = fakegen.name()
		name = tmp_name.split(" ", 1)
		email = fakegen.email()

		user = User.objects.get_or_create(first_name=name[0], last_name=name[1], email=email)[0]



if __name__ == "__main__":
	print("Populating the database... Please Wait")
	populate(20)
	print("Populating Complete")