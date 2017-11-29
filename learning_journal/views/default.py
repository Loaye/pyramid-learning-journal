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
    if request.method == "POST" and request.POST:
        form_names = [ 'title', 'body' ]
        form_data = request.POST
        new_entry = Journal(
            title=request.POST['title'],
            creation_date=datetime.now().strftime('%B %d, %Y'),
            body=request.POST['body']
        )
        request.dbsession.add(new_entry)
        return{}
    data = request.POST
    return data


@view_config(route_name='update', renderer='../templates/update.jinja2')
def update_view(request):
    """Show single blog post."""
    post_id = int(request.matchdict['id'])
    post = request.dbsession.query(Journal).get(post_id)
    if not post:
        return HTTPNotFound
    if request.method == "GET":
        return{
            "title": "Update",
            "post": post,
        }
    if request.method == "POST":
        post.title = request.POST['title']
        post.body = request.POST['body']
        request.dbsession.add(post)
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail', id=post_id))