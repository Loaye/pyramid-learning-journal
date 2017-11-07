"""Set the default for the app."""
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.data.entry_data import ENTRIES


@view_config(route_name="home", renderer="../templates/list.jinja2")
def list_view(request):
    """Home Page."""
    entry = request.dbsession.query(learning_journal).all()
    if entry is NONE:
        raise HTTPNotFound
    return {
        "entries": ENTRIES
    }


@view_config(route_name="detail", renderer="../templates/detail.jinja2")
def detail_view(request):
    """Show single blog post."""
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(learning_journal).get(entry_id)
    for entry in ENTRIES:
        if entry["id"] == entry_id:
            return{"entry" : entry }


@view_config(route_name="create", renderer="../templates/create.jinja2")
def create_view(request):
    """Create a new blog post."""
    return {
       
    }


@view_config(route_name="update", renderer="../templates/update.jinja2")
def update_view(request):
    """Update an existing blog entry."""
    return {
        "entries": id
    }
