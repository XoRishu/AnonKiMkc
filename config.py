import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "10872193"))
API_HASH = getenv("API_HASH", "7a2c777e52479d13fb1adb29944130cf")

BOT_TOKEN = getenv("BOT_TOKEN", "5765373620:AAGBPtghJGCqs7OxGOwLGtNALEI2XeYWRJ4")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://rishu:rishu@rishu.yvvefj7.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001607942799"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Yorha X Music")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5205602399").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/XoRishu/AnonKiMkc")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Kanna_Updates")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Kanna_Support")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bd868f78a92b4734b7b0fde505df0c71")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2c68c32bc55249d4b690e2d89223bf63")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQBIY9UlvWax2DCBU7eQLnBy9gSk9NdQ23F-aKdBvsHeyCWmryDj4ca52oDLlgT4b5ZUedvaabf-CXKnQKWiJkaxVT-2-XzkP_kFo29x_Nl2OaYl2SWH1PH3buASVM7ucfkoVMWHbDuBp7yYFnDyTzCHvpDTbnrZKlQL5u21cAu82gpyoP9eHVmtynVQ1Ch-7yjCLP3mt9l0_7KgPZAg5F_Ip4SlDe_SvESgnoCy_UJ0HRRkpUrqLmo0bqvCvpPZiEwZMTIHDh8sLKdWws4ibITYylWmEIRU6tFUdNR93miEIchFGlvyA5xprmtPvmFyn8sjCJ2--n8V8Jkb4jSo2ReeAAAAATPZmXAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/2b2358337a5142456a6c1.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/7967d3a3dad34c8fb7398.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/6a782ca451a8e6136371a.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/815475579371a6f34cad6.jpg"

STATS_IMG_URL = "https://telegra.ph/file/a8cad5a20a9597d793ba4.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/8fb53cefcfa1847434e1a.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/6ee9f83b8c41f9c07e1ea.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/1d8641424badab1ff702d.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/cebd97658ddc5bfb3912d.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/5d419f7313a0af834f955.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/4a67d2c2f2c41f4a58113.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/aec87b99c77680032b3a2.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/5c1f180351ad1c91b022b.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/7967d3a3dad34c8fb7398.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/2b2358337a5142456a6c1.jpg"
