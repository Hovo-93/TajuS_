from faker import Faker

from usersdata.models import User
import faker.providers

ROLES = [
    "ADMIN",
    "USER"
]


class Provider(faker.providers.BaseProvider):
    def role(self):
        return self.random_element(ROLES)


fake = Faker(['ru_RU'])


def generate_users(count):
    fake.add_provider(Provider)
    for _ in range(count):
        user = User.objects.create_user(
            username=fake.name(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birthday=fake.date(),
            email=fake.email(),
            role=fake.role()
        )
        user.save()
