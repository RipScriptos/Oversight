import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 12001))