import datetime
import pylast

API_KEY=''
API_SECRET=''
DOWNLOAD_LIMIT = 50;

class Container(object):
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

def printScrobbles(scrobbles):
  for scrobble in scrobbles:
    print('[{}] {} - {}'.format(datetime.datetime.fromtimestamp(int(scrobble.timestamp)), scrobble.track.artist, scrobble.track.title))

def getScrobbles(user, lastDays = 7):
  timeTo = datetime.datetime.now() + datetime.timedelta(days=1) #to tommorow (just to ensure that current track will be included)
  timeFrom = datetime.datetime.now() - datetime.timedelta(days=lastDays)
  timestampTo = timeTo.timestamp()
  timestampFrom = timeFrom.timestamp()
  network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
  result = []
  while True:
    scrobbles = network.get_user(user).get_recent_tracks(limit = DOWNLOAD_LIMIT, time_to = timestampTo, time_from = timestampFrom)
    result.extend(scrobbles)
    if len(scrobbles) < DOWNLOAD_LIMIT-1:
      return result
    timestampTo = min(s.timestamp for s in scrobbles)

def getScrobbleStatistic(scrobbles):
  return Container(count = len(scrobbles),
                   artists_count = len(set(s.track.artist for s in scrobbles)),
                   tracks_count = len(set('{}{}'.format(s.track.artist,s.track.title) for s in scrobbles)))
      
def compare(user1, user2, interval):
  scrobbles1 = getScrobbles(user1, lastDays = interval)
  stat1 = getScrobbleStatistic(scrobbles1)
  print('User {} scrobbled {} times for last {} days.'.format(user1, stat1.count, interval))
  print('Unique tracks: {}. Unique artists: {}.'.format(stat1.tracks_count, stat1.artists_count))
  #printScrobbles(scrobbles)

  print()

  scrobbles2 = getScrobbles(user2, lastDays = interval)
  stat2 = getScrobbleStatistic(scrobbles2)
  print('User {} scrobbled {} times for last {} days.'.format(user2, stat2.count, interval))
  print('Unique tracks: {}. Unique artists: {}.'.format(stat2.tracks_count, stat2.artists_count))
  #printScrobbles(scrobbles)


compare('K0t0wsk1', 'moehikka', 7)