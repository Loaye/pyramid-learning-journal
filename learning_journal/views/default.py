"""Set the default for the app."""
from pyramid.view import view_config
from learning_journal.data.entry_data import ENTRIES


@view_config(route_name="list_view", renderer="../templates/list_view.jinja2")
def list_view(request):
    """Home Page."""
    return {
        "entries": ENTRIES
    }


@view_config(route_name="create_view", renderer="../templates/create_view.jinja2")
def create_view(request):
    """Create a new blog post."""
    return {
        "entries": ENTRIES
    }


@view_config(route_name="detail_view", renderer="../templates/route_view.jinja2")
def detail_view(request):
    """Show single blog post."""
    return {
        "entries": ENTRIES
    }


@view_config(route_name="update_view", renderer="../templates/update_view.jinja2")
def update_view(request):
    """Update an existing blog entry."""
    return {
        "entries": ENTRIES
    }
