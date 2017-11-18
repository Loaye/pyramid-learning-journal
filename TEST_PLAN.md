#Tests for Step 1
```
def test_list_view_response_status_code_200_ok(dummy_request):
    """Test if request will return 200 ok response."""
    response = list_view(dummy_request)
    assert response.status_code == 200


def test_datail_view_response_status_code_200_ok(dummy_request):
    """Test if request will return 200 ok response."""
    response = detail_view(dummy_request)
    assert response.status_code == 200


def test_create_view_response_status_code_200_ok(dummy_request):
    """Test if request will return 200 ok response."""
    response = create_view(dummy_request)
    assert response.status_code == 200


def test_update_view_response_status_code_200_ok(dummy_request):
    """Test if request will return 200 ok response."""
    response = update_view(dummy_request)
    assert response.status_code == 200
```

#Tests for Step 2
```
def test_list_view_response_text_has_proper_content_type(dummy_request):
    """Test that list view returns expected content."""
    response = list_view(dummy_request)
    assert response.content_type == 'text/html'


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
```

#Tests for Step 3
```
def test_model_gets_added(db_session):
    """Test to see if model gets added to database."""
    assert len(db_session.query(Journal).all()) == 0
    model = Journal(
        title="Fake Title",
        body="Fake Body",
        creation_date=datetime.now()
    )
    db_session.add(model)
    assert len(db_session.query(Journal).all()) == 1

def test_list_view_returns_dict(dummy_request):
    """Home view returns a dictionary of values"""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)

def test_list_view_returns_empty_when_database_empty(dummy_request):
    """List view returns nothing when there is no data."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert len(response['entries']) == 1

def test_list_view_returns_count_matching_database(dummy_request):
    """Home view response matches database count."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    query = dummy_request.dbsession.query(Journal)
    assert len(response['entries']) == query.count()
```

#Tests for Step 4