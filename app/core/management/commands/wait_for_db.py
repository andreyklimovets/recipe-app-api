"""
Django command to wait for database to be available.
"""

import time

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Wait for db class"""

    def handle(self, *args, **options):
        """ Db cheker. """
        self.stdout.write('Database is starting!')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database is not ready, try again in 1 sec')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
