from django.core.management.base import BaseCommand
from usersdata.generate_user_data import generate_users


class Command(BaseCommand):
    help = "Populate MyModel with fake data"

    def handle(self, *args, **options):
        generate_users(10)
        print('Completed')
