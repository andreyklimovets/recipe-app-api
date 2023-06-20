"""
Django command to wait for database to be available.
"""
from django.core.management.commands import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        pass