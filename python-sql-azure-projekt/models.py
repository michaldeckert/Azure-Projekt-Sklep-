from sqlalchemy import Column, Integer, String, Date


from database import Base


class Wyposazenie(Base):
    __tablename__ = "wyposazenie"

    id = Column(Integer, primary_key=True)
    nazwa = Column(String)
    wykonawca = Column(String)
    gatunek = Column(String)
    nosnik = Column(String)
    wydawnictwo = Column(String)
    wydano = Column(Date)
