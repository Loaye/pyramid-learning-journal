"""Set the default for the app"""
from pyramid.response import Response
import io
import os

HERE = os.path.dirname(__file__)

def list_view(request):
    """Home Page."""
    path = os.path.join(HERE, '../templates/list_view.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read)


def create_view(request):
    """Create a new blog post."""
    path = os.path.join(HERE, '../templates/create_view.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read)


def detail_view(request):
    """Show single blog post."""
    path = os.path.join(HERE, '../templates/detail_view.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read)


def update_view(request):
    """Update an existing blog entry."""
    path = os.path.join(HERE, '../templates/update_view.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read)
