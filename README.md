# Pyramid Learning Journal

## STEP 1
### Summary
------------
Step 1 creates a basic scaffold using *Pyramid*, *CookieCutter*, and *Jinja*. We set our project to be a learning journal. This learning journal will show a lists of daily entries and our personal discoveries with Python. Some entry's may be a little dim, but we just want to track our progess.

We determined that we wanted to use a template for the front end so *Pyramid* jumped out to us. We liked the idea to create a layout and be able to template in information based off of CRUD(Create, Read, Update, & Destroy). Having four views to be able to look at an entry, edit, update, and destroy made it a perfect use for this app.

## STEP 2
### What's going on here?
---------------------------

Step 1 is creating the scaffold with MVR(Model, Views, & Routes) with CRUD in mind for a control aspect. We set in our models, views, and routes.

Model will hold the basic structure.
Model Ex.
```class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)
```

View will be what is displayed to the DOM.
View Ex.
```
{% extends "layout.jinja2" %}

{% block content %}
{% if entries %}
    {% for entry in entries %}
        <article>
            <h2><a href="{{ request.route_url('detail', id=entry.id) }}">{{ entry.title }}</a></h2>
            <p>Created <strong>{{ entry.creation_date }}</strong></p>
            <p>{{ entry.body }}</p>
        </article>
    {% endfor %}
{% else %}
    <p>No entries present, please add an entry to view an entry.</p>
{% endif %}
{% endblock %}
```


## Authors
* [Jacob Carstens](https://github.com/Loaye)
* [Marco Zangari](https://github.com/marco-zangari)