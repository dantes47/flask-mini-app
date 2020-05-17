import os

class Config:
    DEBUG=True
    SECRET_KEY=os.environ['SECRET_KEY']