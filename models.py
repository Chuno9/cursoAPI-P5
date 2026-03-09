from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    __tablename__="todos"

    id=Column(Integer, primary_key=True, index=True)
    titulo=Column(String)
    descripcion=Column(String)
    prioridad=Column(Integer)
    completada=Column(Boolean, default=False)