import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "18955362"))
API_HASH = getenv("API_HASH", "3a63a8decd12cd668283d43dbce20a96")

BOT_TOKEN = getenv("BOT_TOKEN", "5662659781:AAEnPmXa6KsvFx8K46xNVxBuPLeHARnJkZE")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://userbot:userbot@cluster0.x6kstu2.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001246079685"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Dora")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5898166383").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/kuchnhihai/reeder")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NOOBXCREATOR")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/NOOBCREATOR")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "59920"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "14180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "5984fde29e024b308d8defa276e4a601")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "561c1883f2974ff8b03087343e4b0ff8")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "50"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BAA-XVoBfJXdwnRJp9DnJzSA98Trog6RJYwLO_17CYNNI_hK1f7WGkv9eQ9dSw0_4g0JyhTG3heWQUemzwFK3NIgtBcn-w8rFw9IowVNEunSV2lxlBzOI6E7_L0EeZlWO8U9UDZdNC_sr0x4z9VrliDFH5PpyvOyzibdv1mXJ4ApSYUblzsdH2Rvg9YWgT2q_E-rICurNebvR6J5MWpwE_1DVLCWXV155NjV2-Ia2g92t9fZTVtR-v8-xYnX7_CaOcxGwnUTwhVlD3kkvtkZiVngyFSeGxhnPwYw5RMfqwn_HESoLM5oXQJl6l_D8Xgo9JFF5GZMCIGikSEAC-VtNiAAAAAZ93N4MA")
STRING2 = getenv("STRING_SESSION2", "BAAW_xyJTVAGDxqzhkl6Gn8huUMNIZXFIuED4iog2v7RQHFwyxtGHgVPCBkw3qSWnujwXB1CXtMwEIVz0OT-NQYToumk-Eszd96WWhavc07nh3r027N_MJU8WFMIhemvlDCUeSAYCdu-SEa585ZzlWLVTR0Qx6nBBLbsQCq_OpHxPvJut2DYAhhq91-H-EoNX8XuAoOG2wC8p2jzh8US9Pk9Sb0v85I2cBfvMO8SFl71cZx7Xt2pj8HSDqeLMSTpJVSoF3DaCk2q2pqHGbKcndvxxRb3_l8CyTSPErWsF30NKUKhSNTjU2tp3lRxOle3LuvPd9vvo0BX4e2E0O7pV1q1AAAAAZeKir0A")
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


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"


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
            PING_IMG_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/5b7d5f34f7b174e05d447.jpg"
