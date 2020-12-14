import re
import os
import spotipy


def run(message, self_id):
    
    command = re.sub('<@!?\d+>[ ]?', '', message.content).strip()

    search_regex = '^({})'.format('|'.join(['play', 'queue', 'next', 'stop', 'help']))
    keyword = re.findall(search_regex, command, flags=re.IGNORECASE)
    action = keyword[0].lower() if keyword else None

    message_out = None
    embed_out = None
    
    if action is None or action == 'help':
        
        message_out = ''
        if action is None:
            message_out += 'I don\'t understand!\n\n'
        message_out += 'Queue a song:\n\t<@{}> queue Michael Jackson Thriller\n\nPlay a song immediately:\n\t<@{}> play Queen Bohemian Rhapsody\n\nPlay next song in queue:\n\t<@{}> next\n\nPause/stop playback:\n\t<@{}> stop\n\n'.format(*[self_id for i in range(4)])

    else:
        
        spotify = spotipy.Spotify(
            auth_manager=spotipy.oauth2.SpotifyOAuth(
                client_id=os.getenv('SPOTIFY_CLIENT_ID'),
                client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
                redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
                scope="streaming")
        )
        
        if action == 'next':
            spotify.next_track(device_id=os.getenv('SPOTIFY_DEVICE_ID'))
            message_out = 'Next track'
            
        elif action == 'stop':
            spotify.pause_playback(device_id=os.getenv('SPOTIFY_DEVICE_ID'))
            message_out = 'Pause playback'

        else:
            search = re.sub('^{}[ ]?'.format(keyword[0]), '', command).strip()
            spotify_uri = None
            album_art = None

            if search:
                results = spotify.search(q=search, limit=5)
                
                if len(results['tracks']['items']) > 0:
                    top_track = results['tracks']['items'][0] 
                    artist, title = top_track['artists'][0]['name'], top_track['name']
                    try:
                        album_art = top_track['album']['images'][0]['url']
                    except:
                        pass
                    spotify_uri = 'spotify:track:{}'.format(top_track['id'])
                
                else:
                    message_out = 'Nothing found! Try another search...'
                    spotify_uri = -1

            if spotify_uri != -1:  
                
                if action == 'play':
                    
                    if spotify_uri is not None:
                        spotify.start_playback(uris=[spotify_uri], device_id=os.getenv('SPOTIFY_DEVICE_ID'))
                        message_out = 'Play {} by {}'.format(title, artist)
                    else:
                        spotify.start_playback(device_id=os.getenv('SPOTIFY_DEVICE_ID'))
                        message_out = 'Resume playback'
                        
                elif action == 'queue':
                    
                    if spotify_uri is not None:
                        spotify.add_to_queue(spotify_uri, device_id=os.getenv('SPOTIFY_DEVICE_ID'))
                        message_out = 'Queue {} by {}'.format(title, artist)
                
                if album_art is not None:
                    embed_out = album_art

    return message_out, embed_out

