from pydantic import BaseModel


class Company(BaseModel):
    """
    """
    inn: str
    kpp: str
    okved: str
    name: str
    full_name: str
