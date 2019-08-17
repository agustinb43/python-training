from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from fixture import todos
from python_app.todo import Todo
import logging


class TestConfig:

    def setUp(self):
        self.engine = create_engine('sqlite:///test.db', echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self._load_fixture()
        self.session.begin_nested()

    def _store_fixture_data(self, model, items):
        try:
            table = model.__table__
            self.session.execute(table.insert().values(items))
            self.session.commit()
        except Exception as e:
            #logger.error(e, exc_info=True)
            pass

    def _load_fixture(self):
        self._store_fixture_data(Todo, todos)

    def tearDown(self):
        self.session.rollback()
        self.session.close()
