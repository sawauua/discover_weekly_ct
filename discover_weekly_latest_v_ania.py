# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:55:02 2022

"""
from typing import List, Dict
import random

def read_dataset(path):
    """
    Reads a csv file and transforms it into a list of dictionaries with data about every song.
    :returns: a list of dictionaries (songs).
    """
    
    #open file
    file = open(path)
    
    #create keys: I have to hardcode the keys because the commas used in the dataset file don't always work as seprators
    song_keys = tuple(['title', 'artist','genre', 'year', 'BPM', 'Energy', 'Danceability', 'Loudness', 'Liveness', 'Valence', 'Length', 'Acousticness', 'Speechiness', 'Popularity'])
    
    #prepare result list and read the first line (with keys) to omit treating it as a song
    result = []
    line = file.readline()
    
    #read the file line by line
    for line in file:
        new_line = line.strip().replace('"', '').split(',')
        newer_line = []
            
        #transfom string values into integers when possible    
        for i in new_line:
            try:
                newer_line.append(int(i))
            except ValueError:
                newer_line.append(i)
                
        #correcting the data in case of song titles that include commas:
        #If the element at index 3 (corresponding to year) is a string, that means we divided the title into too many parts, making the newer_line list too long.
        #We decided to merge the fisrt list indices up until the value at third index is an integer (it should, because it's the year of release)
        while isinstance(newer_line[3], str):
            title = newer_line[0] + ', ' + newer_line[1]
            newer_line[0] = title
            newer_line.pop(1)
                
        #create a dictionary for a song with prepared keys and values        
        my_dict = dict(zip(song_keys, newer_line))
        
        #add the dictionary to the result list
        result.append(my_dict)
        
        #convert song titles to strings in case they were converted to int in line 33
        for i in range(len(result)):
            result[i]['title'] = str(result[i]['title'])
        
    return result

def song_in_playlist(playlist, criterion, song):
    """
    Looks for a specifc song (by criterion) in a playlist.

    Args:
        sorted_playlist (TYPE): DESCRIPTION.
        song (TYPE): DESCRIPTION.

    Returns:
        None.

    """
    #sort based on criterion
    playlist = sort_playlist(playlist, criterion)
    
    #binary serach through a sorted playlist
    upper_bound = len(playlist) - 1
    lower_bound = 0
    
    while lower_bound <= upper_bound:
        mid = int((upper_bound + lower_bound) / 2)
        
        if song[criterion] == playlist[mid][criterion]:
            #print(f'found {song} at playlist[{mid}]')
            return True
        
        elif song[criterion] > playlist[mid][criterion]:
            lower_bound = mid + 1
            #print(f'{song} is bigger than {playlist[mid][criterion]}. Reducing search to the upper half.')
        
        else:
            upper_bound = mid - 1
            #print(f'{song} is smaller than {playlist[mid][criterion]}. Reducing search to the lower half.')
        
    return False

def playlists(songs):
    playlists = []
    for i in range(100):
        playlist = []
        for j in range(50):
            randsong = songs[random.randint(0,len(songs) - 1)]
            while randsong in playlist:
                randsong = songs[random.randint(0,len(songs) - 1)]
            playlist.append(randsong)
        playlists.append(playlist)
            
    return playlists

def sort_playlist(playlist, criterion):
    """
    Sorts a playlist based on the given criterion. Criterion can be any key (title, artist, BPM, Speechiness etc.)

    Args:
        playlist (TYPE): DESCRIPTION.
        criterion (TYPE): DESCRIPTION.

    Returns:
        None.

    """
    
    for i in range(len(playlist) - 1):
        
        for j in range(len(playlist) - i - 1):
            
            if playlist[j][criterion] > playlist[j+1][criterion]:
                
                helper = playlist[j]
                playlist[j] = playlist[j+1]
                playlist[j+1] = helper
                
    return playlist

def users(n, songs):
    users = []
    for i in range(n):
        user_list = []
        for j in range(random.randint(0, len(songs)-1)):
            user_list.append(songs[random.randint(0,len(songs) - 1)])
        users.append(user_list)
            
    return users

def users2(n: int, songs: List[Dict[str,any]]) -> Dict[str, List[str]]:
    users = {}
    for i in range(1,n+1):
        user_list = []
        for j in range(random.randint(0, len(songs)-1)):
            user_list.append(songs[random.randint(0,len(songs) - 1)])
        users[f'user{str(i)}'] = user_list
            
    return users
        
#checking if the read_dataset method works
songs = read_dataset('spotify-dataset.csv')
# for i in range(len(songs)):
#     print(songs[i]['title'])


#checking if the sort_playlist method works
"""playlist1 = [{'title': 'Hey,  Soul Sister', 'artist': 'Train', 'genre': 'neo mellow', 'year': 2010, 'BPM': 97, 'Energy': 89, 'Danceability': 67, 'Loudness': -4, 'Liveness': 8, 'Valence': 80, 'Length': 217, 'Acousticness': 19, 'Speechiness': 4, 'Popularity': 83}, {'title': 'Love The Way You Lie', 'artist': 'Eminem', 'genre': 'detroit hip hop', 'year': 2010, 'BPM': 87, 'Energy': 93, 'Danceability': 75, 'Loudness': -5, 'Liveness': 52, 'Valence': 64, 'Length': 263, 'Acousticness': 24, 'Speechiness': 23, 'Popularity': 82}, {'title': 'TiK ToK', 'artist': 'Kesha', 'genre': 'dance pop', 'year': 2010, 'BPM': 120, 'Energy': 84, 'Danceability': 76, 'Loudness': -3, 'Liveness': 29, 'Valence': 71, 'Length': 200, 'Acousticness': 10, 'Speechiness': 14, 'Popularity': 80}, {'title': 'Bad Romance', 'artist': 'Lady Gaga', 'genre': 'dance pop', 'year': 2010, 'BPM': 119, 'Energy': 92, 'Danceability': 70, 'Loudness': -4, 'Liveness': 8, 'Valence': 71, 'Length': 295, 'Acousticness': 0, 'Speechiness': 4, 'Popularity': 79}, {'title': 'Just the Way You Are', 'artist': 'Bruno Mars', 'genre': 'pop', 'year': 2010, 'BPM': 109, 'Energy': 84, 'Danceability': 64, 'Loudness': -5, 'Liveness': 9, 'Valence': 43, 'Length': 221, 'Acousticness': 2, 'Speechiness': 4, 'Popularity': 78}, {'title': 'Baby', 'artist': 'Justin Bieber', 'genre': 'canadian pop', 'year': 2010, 'BPM': 65, 'Energy': 86, 'Danceability': 73, 'Loudness': -5, 'Liveness': 11, 'Valence': 54, 'Length': 214, 'Acousticness': 4, 'Speechiness': 14, 'Popularity': 77}, {'title': 'Dynamite', 'artist': 'Taio Cruz', 'genre': 'dance pop', 'year': 2010, 'BPM': 120, 'Energy': 78, 'Danceability': 75, 'Loudness': -4, 'Liveness': 4, 'Valence': 82, 'Length': 203, 'Acousticness': 0, 'Speechiness': 9, 'Popularity': 77}, {'title': 'Secrets', 'artist': 'OneRepublic', 'genre': 'dance pop', 'year': 2010, 'BPM': 148, 'Energy': 76, 'Danceability': 52, 'Loudness': -6, 'Liveness': 12, 'Valence': 38, 'Length': 225, 'Acousticness': 7, 'Speechiness': 4, 'Popularity': 77}, {'title': 'Empire State of Mind (Part II) Broken Down', 'artist': 'Alicia Keys', 'genre': 'hip pop', 'year': 2010, 'BPM': 93, 'Energy': 37, 'Danceability': 48, 'Loudness': -8, 'Liveness': 12, 'Valence': 14, 'Length': 216, 'Acousticness': 74, 'Speechiness': 3, 'Popularity': 76}]
for i in range(len(playlist1)):
     print(playlist1[i]['title'])  
print('')   
sortedp = sort_playlist(playlist1, 'title')
print(sortedp)
for i in range(len(sortedp)):
    print(sortedp[i]['title'])"""



our_users = users2(3,songs)
playlists_100 = playlists(songs)
#print titles of user1's songs
"""print(our_users['user1'])
for i in our_users:
    for j in range(len(i)):
        print(our_users[f'{i}'][j]['title'])"""

def week1(user, playlists):
    yes = 0
    no = 0 # i added this, cause they ask for 3 songs the user has listened to and 3 he hasn't.
    recommendation = []
    for playlist in playlists:
        for song in user:
            if song_in_playlist(playlist, 'title', song):
                #print(song['title'])
                yes += 1
            else:
                no+=1
            if yes >= 3 and no >=3:
                while len(recommendation) < 5:
                    discover_song = playlist[random.randint(0, len(playlist) - 1)]
                    if discover_song not in recommendation:
                        recommendation.append(playlist[random.randint(0, len(playlist) - 1)])
                return recommendation
    
    return 'no match found'

#print random week1 function output
# discover_weekly = week1(users['user2'], playlists_100))
                
#create a non-random list of playlists and a user to check week1 funtion

playlists_nonran = [songs[:10], songs[15:20], songs[30:45], songs[150:200], songs[367:370]]
our_users['user_nonran'] = songs[25:400]
# print(week1(our_users['user_nonran'], playlists_nonran))


genre_list = [] # len = 50
pop = [] # len = 18
techno = [] # len = 5
rocking = [] # len = 1
other_genres = [] # len = 26

for i in range(len(songs)):
    if songs[i]['genre'] not in genre_list:
        genre_list.append(songs[i]['genre'])

for genre in genre_list:
    if 'pop' in genre:
        pop.append(genre)
    elif 'edm' in genre:
        techno.append(genre)
    elif 'electro' in genre:
        techno.append(genre)
    elif 'rock' in genre:
        rocking.append(genre)
    else:
        other_genres.append(genre)

# print out the genres and the length of each list of genre
'''print(genre_list,'\n',len(genre_list))
print('\n')
print(pop,'\n',len(pop))
print('\n')
print(techno,'\n',len(techno))
print('\n')
print(rocking,'\n',len(rocking))
print('\n')
print(other_genres,'\n',len(other_genres))'''

def genre_filter(playlist):
    for song in playlist:
        if 'pop' in song['genre']:
            song['genre'] = 'pop'
        elif 'edm' in song['genre']:
            song['genre'] = 'techno'
        elif 'electro' in song['genre']:
            song['genre'] = 'techno'
        elif 'rock' in song['genre']:
            song['genre'] = 'rock'
        else:  
            song['genre'] = 'other'
    return playlist

def week2(user: List[Dict[str, any]], playlists: List[List[Dict[str,any]]], three_genres) -> List[Dict[str, any]]:

    recommendation = []
    user = genre_filter(user)
    print(len(user))
    pop = 0
    techno = 0
    rock = 0
    for song in user:
        if song['genre'] == 'pop':
            pop+=1
        elif song['genre'] == 'techno':
            techno+=1
        elif song['genre'] == 'rock':
            rock+=1
    pop_nr = int((pop/len(user))*5)
    rock_nr = int((rock/len(user))*5)
    techno_nr = int((techno/len(user))*5)
    print(techno_nr)
    pop_list = []
    playlist = week1(user, playlists)
    #if len(count_genres(playlist)['pop']) < pop_nr
    while len(pop_list) < pop_nr:
        for song in playlist:
            if song['genre'] == 'pop':
                print(song)
                pop_list.append(song)
    rock_list = []
    while len(rock_list) < rock_nr:
        for song in playlist:
            if song['genre'] == 'rock':
                print(song)
                rock_list.append(song)
    techno_list = []
    while len(techno_list) < techno_nr:
        for song in playlist:
            if song['genre'] == 'techno':
                print(song)
                rock_list.append(song)
                
    recommendation = rock_list + pop_list + techno_list
    return recommendation
    

   # this part doesn't work for some reason beacuse when i try running the function i get an infinite loop.
    """for playlist in playlists:
        playlist = genre_filter(playlist)
        for song in playlist:
            while len(recommendation) < 5:
                if song['genre'] == fav_genre:
                    recommendation.append(song)"""
        
    return recommendation    

def count_genres(playlist):
    genres_dict = {}
    for song in playlist:
        if song['genre'] in genres_dict:
            genres_dict[song['genre']] += 1
        else:
            genres_dict[song['genre']] = 1
        
    return genres_dict

three_genres = {'rock': ['neo mellow', 'british soul', 'permanent wave', 'alaska indie', 'alternative r&b'], 'techno' : ['big room', 'electro', 'complextro', 'house', 'tropical house','belgian edm', 'electronic trap', 'electro house', 'downtempo', 'edm'], 'pop': ['boy band', 'canadian hip hop', 'chicago rap', 'australian hip hop', 'australian dance', 'hollywood', 'canadian contemporary r&b', 'irish singer-songwriter', 'hip hop', 'latin', 'canadian latin', 'brostep', 'contemporary country', 'escape room']}
genres = list(count_genres(songs).keys())
for element in genres:
    if 'pop' in element:
        three_genres['pop'].append(element)
    elif 'rock' in element:
        three_genres['rock'].append(element)
        
        
def classify_mood(playlist):
    for song in playlist:
        song['mood'] = []
        if song['Energy'] > 80 and song['Popularity'] > 50 and song['Valence'] > 80:
            song['mood'].append('happy')
        if song['BPM'] > 100 and song['Energy'] > 85 and song['Danceability'] > 70 and song['Popularity'] > 50:
            song['mood'].append('party')
        if song['BPM'] < 120 and song['Energy'] < 70 and song['Loudness'] < -5 and song['Popularity'] > 50:
            song['mood'].append('chill')
        if song['Acousticness'] > 10 and song['Speechiness'] < 5 and song['Energy'] < 75 and song['Danceability'] < 60:
            song['mood'].append('lounge')
            
    return playlist

def count_moods(playlist):
    happy = 0
    party = 0
    chill = 0
    lounge = 0
    for song in playlist:
        if 'happy' in song['mood']:
            happy += 1
        if 'party' in song['mood']:
            party += 1
        if 'chill' in song['mood']:
            chill += 1
        if 'lounge' in song['mood']:
            lounge += 1
    return {'happy': happy, 'party': party, 'chill': chill, 'lounge': lounge}
    
            
def week3(user, playlists): 
    recommendation = []
    songs_moods = classify_mood(user)
    user_moods = count_moods(songs_moods)
    divisor = user_moods['happy'] + user_moods['party'] + user_moods['chill'] + user_moods['lounge']
    ratio = [round((user_moods['happy']/divisor) * 5), round((user_moods['party']/divisor) * 5), round((user_moods['chill']/divisor) * 5), round((user_moods['lounge']/divisor) * 5)]
    for playlist in playlists:
        playlist_moods = count_moods(classify_mood(playlist))
        if playlist_moods['happy'] > ratio[0] and  playlist_moods['party'] > ratio[1] and playlist_moods['chill'] > ratio[2] and playlist_moods['lounge'] > ratio[3]:
            for song in playlist:
                if len(recommendation) < ratio[0]:
                    if 'happy' in song['mood']:
                        recommendation.append(song)             
            for song in playlist:
                if len(recommendation) < ratio[1] + ratio[0]:
                    if 'party' in song['mood']:
                        recommendation.append(song)
            for song in playlist:
                if len(recommendation) < ratio[1] + ratio[0] + ratio[2]:
                     if 'chill' in song['mood']:
                         recommendation.append(song)
            for song in playlist:
                if len(recommendation) < ratio[1] + ratio[0] + ratio[2] + ratio[3]:
                     if 'lounge' in song['mood']:
                         recommendation.append(song)
            return recommendation
            
        
print(week3(our_users['user2'], playlists_100))
print(len(week3(our_users['user2'], playlists_100)))