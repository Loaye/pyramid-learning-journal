from sqlalchemy import (
    Column,
    DateTime,
    Index,
    Integer,
    Text,
    Unicode
)

from .meta import Base


class Journal(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    creation_date = Column(DateTime)

    # def push_to_dict(self):
    #     """Pushes attributes to the dictionary."""
    #     "id": self.id,
    #     "title": self.title,
    #     "body": self.body,
    #     "creation_date": self.creation_date
