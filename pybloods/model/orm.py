"""
Initialise API
"""

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class NoteGroup(Base):
    __tablename__ = 'note_group'

    note_group_id = Column(Integer, primary_key=True, autoincrement='auto')


class Note(Base):
    __tablename__ = 'note'

    note_id = Column(Integer, primary_key=True, autoincrement='auto')
    note_group_id = Column(Integer, ForeignKey('note_group.note_group_id'))


class Provider(Base):
    __tablename__ = 'provider'

    provider_id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String)


class Source(Base):
    __tablename__ = 'source'

    source_id = Column(Integer, primary_key=True, autoincrement='auto')
    provider_id = Column(Integer, ForeignKey('provider.provider_id'))
    lab_id = Column(Integer, ForeignKey('lab.lab_id'))


class Sample(Base):
    __tablename__ = 'sample'

    sample_id = Column(Integer, primary_key=True, autoincrement='auto')
    taken_at = Column(DateTime())
    source_id = Column(Integer, ForeignKey('source.source_id'))


class Observation(Base):
    __tablename__ = 'observation'

    observation_id = Column(Integer, primary_key=True, autoincrement='auto')
    value = Column(Float)
    unit_id = Column(Integer, ForeignKey('unit.unit_id'))
    extracted_at = Column(DateTime())


class Unit(Base):
    __tablename__ = 'unit'

    unit_id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String)


class Lab(Base):
    __tablename__ = 'lab'

    lab_id = Column(Integer, primary_key=True, autoincrement='auto')


# class Pet(Base):
#     __tablename__ = 'pets'
#     id = Column(String(20), primary_key=True, autoincrement='auto')
#     name = Column(String(100))
#     animal_type = Column(String(20))
#     created = Column(DateTime())
#
#     def update(self, id=None, name=None, animal_type=None, tags=None, created=None):
#         if name is not None:
#             self.name = name
#         if animal_type is not None:
#             self.animal_type = animal_type
#         if created is not None:
#             self.created = created
#
#     def dump(self):
#         return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
