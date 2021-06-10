import os 

class Config(object):

  APP_ID = int(os.environ.get("APP_ID", "2980496"))

  API_HASH = os.environ.get("API_HASH", "9415a61fedcc0f00f33667ca46e577a3")

  TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1705260996:AAHfaDQeXP2ft11YF3OR4CMJccTeRxIK5VE")

  AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "Deeks_04_8").split())

  DOWNLOAD_LOCATION = "./bot/DOWNLOADS"

  DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Prorenamer: Prorenamer@renamerpro.2sj6d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

  OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "1086432320").split("1051512795")]

  CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION",False)

  UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "DB_ROBOTS")
