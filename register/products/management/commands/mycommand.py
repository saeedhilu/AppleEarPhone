from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This is my custom command"

    def handle(self, *args: Any, **options: Any) -> None:
        print("This is custom command")
