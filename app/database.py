from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL="sqlite:///./banking.db"
DATABASE_URL = "mysql+pymysql://username:password@localhost/banking_chatbot"
engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
