from sqlalchemy import create_engine, text, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base


connection_string = "mysql+mysqlconnector://testUser:testPassword@localhost:3306/testPythonDb"
engine = create_engine(connection_string, echo=True)

#####################################################################################################
# As raw data
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM TestData"))


    for row in result:
        print(row)


#####################################################################################################
# Using SqlAlchemyORM
        
Base = declarative_base()

class TestUser(Base):
    __tablename__ = "TestData"

    id = Column(String, primary_key=True)
    keyCol = Column(String)
    valueCol = Column(String)

Session = sessionmaker(bind=engine)
session = Session()

for instance in session.query(TestUser).order_by(TestUser.id):
    print(instance)
    print(instance.id, instance.keyCol, instance.valueCol)     