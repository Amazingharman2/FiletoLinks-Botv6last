# 🗿  Visit & Support us - @UHD_Official
# ⚡️ Do Not Remove Credit - Made by @UHD_Bots
# 💬 For Any Help Join Support Group: @UHDBots_Support
# 🚫 Removing or Modifying these Lines will Cause the bot to Stop Working.


import re
from os import environ


id_pattern = re.compile(r'^-?\d+$')


SESSION = environ.get("SESSION", "UHDFiletoLinksBot")
API_ID = int(environ.get("API_ID", "23991460"))
API_HASH = environ.get("API_HASH", "482b9c11ca28fdff8f0d3f9223ef0ac1")
BOT_TOKEN = environ.get("BOT_TOKEN", "7556995516:AAGEVw6A1dm-eW-sOU5Ak_8xghk4Y6_Y744")


PORT = int(environ.get("PORT", "8080"))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
ON_HEROKU = "DYNO" in environ
URL = environ.get("URL", "https://filetolinks-v6harman.onrender.com/")


LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003143688977"))
ADMINS = [
    int(admin) if id_pattern.match(admin) else admin
    for admin in environ.get("ADMINS", "2052400282").split()
]


DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://chpudas:SPNjedirQ26Nungu@clustercompressbot.qnztune.mongodb.net/?retryWrites=true&w=majority&appName=Clustercompressbot")
DATABASE_NAME = environ.get("DATABASE_NAME", "Clustercompressbot")
