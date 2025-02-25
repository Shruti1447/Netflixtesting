from NETFLIXMUSIC.core.bot import SHRUSHTHI
from NETFLIXMUSIC.core.dir import dirr
from NETFLIXMUSIC.core.git import git
from NETFLIXMUSIC.core.userbot import Userbot
from NETFLIXMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SHRUSHTHI()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
