#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys
import warnings
from django.core.management import execute_from_command_line
from django.utils.deprecation import RemovedInDjango50Warning

# Use the new imports to avoid Wagtail deprecation warnings

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opnlend.settings')
    try:
        import django
        django.setup()
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    warnings.filterwarnings("ignore", category=RemovedInDjango50Warning)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opnlend.settings')
    execute_from_command_line(sys.argv)

