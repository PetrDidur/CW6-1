from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='Admin',
            is_superuser=True,
            is_active=True,
            is_staff=True
        )

        user.set_password('9184')
        user.save()