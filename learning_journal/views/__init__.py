"""View routes."""
from learning_journal.views.default import (
    list_view,
    detail_view,
    create_view,
    update_view
)

def includeme(config):
    """Add views for each view and route"""
    config.add_route('list_view', route_name="home")
    config.add_route('detail_view', route_name="detail")
    config.add_route('create_view', route_name="create")
    config.add_route('update_view', route_name="update")
