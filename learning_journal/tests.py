
"""Test default.py."""
from __future__ import unicode_literals
from learning_journal.data.entry_data import ENTRIES
from pyramid import testing
import pytest

from learning_journal.views.default import (
    list_view,
    detail_view,
    create_view,
    update_view,
)

@pytest.fixture(scope="session")
def configure(request):
    """Sets up an instance configure"""
    config = testing.setUp(
        settings={'sqlalchemy.url': 'postgres://localhost:5432/test_learning_journal'})
    config.include("learning_journal.models")
    config.include("learning_journal.routes")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config

# @pytest.fixture(scope="session")
# def db_session(configure, request)
#     """Create a database session"""
#     SessionFactory = 

@pytest.fixture
def dummy_request():
    """Fixture to initiate request for testing."""
    return testing.DummyRequest()


# def test_list_view_response_status_code_200_ok(dummy_request):
#     """Test if request will return 200 ok response."""
#     response = list_view(dummy_request)
#     assert response.status_code == 200


# def test_datail_view_response_status_code_200_ok(dummy_request):
#     """Test if request will return 200 ok response."""
#     response = detail_view(dummy_request)
#     assert response.status_code == 200


# def test_create_view_response_status_code_200_ok(dummy_request):
#     """Test if request will return 200 ok response."""
#     response = create_view(dummy_request)
#     assert response.status_code == 200


# def test_update_view_response_status_code_200_ok(dummy_request):
#     """Test if request will return 200 ok response."""
#     response = update_view(dummy_request)
#     assert response.status_code == 200


# def test_list_view_response_text_has_proper_content_type(dummy_request):
#     """Test that list view returns expected content."""
#     response = list_view(dummy_request)
#     assert response.content_type == 'text/html'


def test_list_view_returns_dict():
    """Home view returns a Response object."""
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, dict)

def test_list_view_returns_proper_amount_of_content():
    """Home view response has file content."""
    request = testing.DummyRequest()
    response = list_view(request)
    assert len(response['entries']) == len(ENTRIES)

def test_list_view():
    """Test that what's returned by the view is a dictionary of values."""
    request = testing.DummyRequest()
    info = list_view(request)
    assert isinstance(info, dict)

def test_detail_view():
    """Test that what's returned by the view is a dictionary of values."""
    request = testing.DummyRequest()
    request.matchdict['id'] = 13
    info = detail_view(request)
    assert isinstance(info, dict)
