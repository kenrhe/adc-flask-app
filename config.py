import os
from pymongo import MongoClient
from dotenv import load_dotenv

if os.environ.get('MONGOLAB_URI') is not None:
	MONGO_URL = os.environ.get('MONGOLAB_URI')
else:
	MONGO_URL = os.getenv("MONGOLAB_URI")

if os.environ.get('APPKEY') is not None:
	APPKEY = os.environ.get('APPKEY')
else:
	APPKEY = os.getenv("APPKEY")

client = MongoClient(MONGO_URL)
