from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
db_user = os.environ.get("POSTGRES_USER")
db_pass = os.environ.get("POSTGRES_PASSWORD")
db_name = os.environ.get("POSTGRES_DB")

print(f'postgresql://{db_user}:{db_pass}@localhost/{db_name}')

#                       dialect+driver://username:password@host:port/database
engine = create_engine(f'postgresql://{db_user}:{db_pass}@localhost/{db_name}')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    #LOAD ENV VARS
    

    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import rest_app.models
    Base.metadata.create_all(bind=engine)