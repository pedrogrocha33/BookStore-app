"""
WSGI config for bookstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

# Define the default settings module for the 'bookstore' project.
# This ensures that the correct settings are used when running the app in production.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")

# Get the WSGI application for the project.
# This is the entry point for WSGI servers (like Gunicorn, uWSGI, etc.) to serve the app.
application = get_wsgi_application()
