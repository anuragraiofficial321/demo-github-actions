from sqlalchemy import Column, Integer, String, Text

class Item():
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    llm_response = Column(Text, nullable=True)