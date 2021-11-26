from django.core.management.base import BaseCommand

from accounts.models import AdminType, User
import logging
logger=logging.getLogger(__name__)
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--username", type=str)
        parser.add_argument("--password", type=str)
        parser.add_argument("--action", type=str)

    def handle(self, *args, **options):
        username = options["username"]
        password = options["password"]
        action = options["action"]

        if not(username and password and action):
            self.stdout.write(self.style.ERROR("Invalid args"))
            exit(1)

        if action == "create_admin":
            if User.objects.filter(id=1).exists():
                self.stdout.write(self.style.SUCCESS(f"User {username} exists, operation ignored"))
                exit()

            user = User.objects.create(username=username, admin_type=AdminType.ADMIN)
            user.set_password(password)
            user.save()

            self.stdout.write(self.style.SUCCESS("User created"))
        elif action == "reset":
            try:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Password is rested"))
            except User.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"User {username} doesnot exist, operation ignored"))
                exit(1)