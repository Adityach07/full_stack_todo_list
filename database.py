from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://kukeqqcd:s3anFmwOyaKvIvVdfEo2wf6MQyBTJmTL@tiny.db.elephantsql.com/kukeqqcd"



engine = create_engine(SQLALCHEMY_DATABASE_URL)

# MYSQL Series
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
