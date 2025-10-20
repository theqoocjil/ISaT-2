from db.db import Base

from neomodel import (
    IntegerProperty, Relationship, StringProperty
)

class Person(Base):
    uid = IntegerProperty(required=True)
    first_name = StringProperty()
    last_name = StringProperty()
    friends = Relationship('Person', 'FRIEND')