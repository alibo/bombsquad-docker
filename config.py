# Name of our server in the public parties list
config['partyName'] = 'FFA'

# If True, your party will show up in the global public party list
# Otherwise it will still be joinable via LAN or connecting by IP address
config['partyIsPublic'] = True

# UDP port to host on. Change this to work around firewalls or run multiple
# servers on one machine.
# 43210 is the default and the only port that will show up in the LAN
# browser tab.
config['port'] = 43210

# Language the server will run in.
# This is no longer terribly relevant, as all clients now see the game in their
# own language. You still may want to override this simply to keep your listing
# accurate however.
config['language'] = 'English'

# Max devices in the party. Note that this does *NOT* mean max players.
# Any device in the party can have more than one player on it if they have
# multiple controllers. Also, this number currently includes the server so
# generally make it 1 bigger than you need. Max-players is not currently
# exposed but I'll try to add that soon.
config['maxPartySize'] = 6

# Options here are 'ffa' (free-for-all) and 'teams'
# this value is only used if you do not supply a playlistCode (see below);
# in that case the default teams or free-for-all playlist gets used
config['sessionType'] = 'ffa'

# To host your own custom playlists, use the 'share' functionality in the
# playlist editor in the regular version of the game.
# This will give you a numeric code you can enter here to host that playlist.
config['playlistCode'] = None

# Whether to shuffle the playlist or play its games in designated order
config['playlistShuffle'] = True

# If True, keeps team sizes equal by disallowing joining the largest team
# (teams mode only)
config['autoBalanceTeams'] = True

# Whether to enable telnet access on port 43250
# This allows you to run python commands on the server as it is running.
# Note: you can now also run live commands via stdin so telnet is generally
# unnecessary. BombSquad's telnet server is very simple so you may have to turn
# off any fancy features in your telnet client to get it to work.
# IMPORTANT: Telnet is not encrypted at all, so you really should not expose
# it's port to the world. If you need remote access, consider connecting to
# your machine via ssh and running telnet to localhost from there.
config['enableTelnet'] = False

# Port used for telnet
config['telnetPort'] = 43250

# This can be None for no password but PLEASE do not expose that to the
# world or your machine will likely get owned.
config['telnetPassword'] = 'changeme'

# Series length in teams mode (7 == 'best-of-7' series; a team must get 4 wins)
config['teamsSeriesLength'] = 7

# Points to win in free-for-all mode (Points are awarded per game based on
# performance)
config['ffaSeriesScoreToWin'] = 24

# If you provide a custom stats webpage for your server, you can use
# this to provide a convenient in-game link to it in the server-browser
# beside the server name.
# if ${ACCOUNT} is present in the string, it will be replaced by the
# currently-signed-in account's id.  To get info about an account,
# you can use the following url:
# http://bombsquadgame.com/accountquery?id=ACCOUNT_ID_HERE
config['statsURL'] = ''
