from django.core.management.base import BaseCommand
from django.test import Client


class Command(BaseCommand):
    help = 'Verify REST API endpoints are available and return data'

    def handle(self, *args, **options):
        client = Client()
        endpoints = ['/api/users/', '/api/teams/', '/api/activities/', '/api/workouts/', '/api/leaderboard/']
        for e in endpoints:
            resp = client.get(e)
            self.stdout.write(f"{e} -> status {resp.status_code}")
            try:
                data = resp.json()
                self.stdout.write(f"  count: {len(data)}")
                if len(data) > 0:
                    self.stdout.write(f"  sample: {data[0]}")
            except Exception:
                self.stdout.write("  no json response or empty")
