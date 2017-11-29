"""Set the default for the app."""
from pyramid.view import view_config
from learning_journal.data.entry_data import ENTRIES
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from learning_journal.models.mymodel import Journal


@view_config(route_name="home", renderer="../templates/list.jinja2")
def list_view(request):
    """Home Page."""
    entry = request.dbsession.query(Journal).all()
    if entry is None:
        raise HTTPNotFound
    return {
        "entries": entry
    }


@view_config(route_name="detail", renderer="../templates/detail.jinja2")
def detail_view(request):
    """Show single blog post."""
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Journal).get(entry_id)
    if entry:
        return {
            "id": entry.id,
            "title": entry.title,
            "body": entry.body,
            "creation_date": entry.creation_date
        }
    else:
        raise HTTPNotFound


@view_config(route_name="create", renderer="../templates/create.jinja2")
def create_view(request):
    """Create a new blog post."""
    if request.method == "POST":
            if not all([field in request.POST for field in ['title', 'body']]):
                raise HTTPBadRequest
            new_entry = Journal(
                title=request.POST['title'],
                creation_date=datetime.now().strftime('%B %d, %Y'),
                body=request.POST['body']
            )
            request.dbsession.add(new_entry)
            return HTTPFound(request.route_url('home'))

    return {}


@view_config(route_name="update", renderer="../templates/update.jinja2")
def update_view(request):
    """Update an existing blog entry."""
    return {
        "entries": id
    }
