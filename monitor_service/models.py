from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Estufa(Base): 
    __tablename__ = 'estufa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    temperatura = Column(Float)
    sensacao_termica = Column(Float)
    umidade = Column(Float)

    def to_dict(self):
        return {
            'id': self.id,
            'temperatura': self.temperatura,
            'sensacao_termica': self.sensacao_termica,
            'umidade': self.umidade
        }
