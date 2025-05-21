from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmarker

DATABASE_URL ="sqlite:///./nuvemshop.db"
engine =creat_engine(DATABASE_URL, connect_args={"check_same_thread: false"})
sessionlocal=sessionmaker(autocommit=false, autoflush=false, binde=engine)
Base = declarative declarative_base()