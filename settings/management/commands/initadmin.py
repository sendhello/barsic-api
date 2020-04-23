from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        for user in settings.ADMINS.split(','):
            username, email, password = user.replace(' ', '').split(':')
            User = get_user_model()
            if not User.objects.filter(username=username).first():
                User.objects.create_superuser(username, email, password)
            else:
                self.stdout.write(self.style.WARNING(f'Пользователь {username} уже существует!'))
