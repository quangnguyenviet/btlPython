from django.core.management.base import BaseCommand
from account.utils import importCustomersFromExcel

class Command(BaseCommand):
    help = 'Import customers from Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        importCustomersFromExcel(file_path)
        self.stdout.write(self.style.SUCCESS('Customers imported successfully!'))