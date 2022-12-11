# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:55:02 2022

"""

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
            print(f'found {song[criterion]} at playlist[{mid}]')
            return True
        
        elif song[criterion] > playlist[mid][criterion]:
            lower_bound = mid + 1
            print(f'{song[criterion]} is bigger than {playlist[mid][criterion]}. Reducing search to the upper half.')
        
        else:
            upper_bound = mid - 1
            print(f'{song[criterion]} is smaller than {playlist[mid][criterion]}. Reducing search to the lower half.')
        
    return False

def playlists(songs):
    playlists = []
    for i in range(100):
        playlist = []
        for j in range(50):
            randsong = songs[random.randint(0,len(songs) - 1)]['title']
            while randsong in playlist:
                randsong = songs[random.randint(0,len(songs) - 1)]['title']
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
            user_list.append(songs[random.randint(0,len(songs) - 1)]['title'])
        users.append(user_list)
            
    return users
        
#checking if the read_dataset method works
songs = read_dataset('spotify-dataset.csv')
print(songs)


#checking if the sort_playlist method works
playlist1 = [{'title': 'Hey,  Soul Sister', 'artist': 'Train', 'genre': 'neo mellow', 'year': 2010, 'BPM': 97, 'Energy': 89, 'Danceability': 67, 'Loudness': -4, 'Liveness': 8, 'Valence': 80, 'Length': 217, 'Acousticness': 19, 'Speechiness': 4, 'Popularity': 83}, {'title': 'Love The Way You Lie', 'artist': 'Eminem', 'genre': 'detroit hip hop', 'year': 2010, 'BPM': 87, 'Energy': 93, 'Danceability': 75, 'Loudness': -5, 'Liveness': 52, 'Valence': 64, 'Length': 263, 'Acousticness': 24, 'Speechiness': 23, 'Popularity': 82}, {'title': 'TiK ToK', 'artist': 'Kesha', 'genre': 'dance pop', 'year': 2010, 'BPM': 120, 'Energy': 84, 'Danceability': 76, 'Loudness': -3, 'Liveness': 29, 'Valence': 71, 'Length': 200, 'Acousticness': 10, 'Speechiness': 14, 'Popularity': 80}, {'title': 'Bad Romance', 'artist': 'Lady Gaga', 'genre': 'dance pop', 'year': 2010, 'BPM': 119, 'Energy': 92, 'Danceability': 70, 'Loudness': -4, 'Liveness': 8, 'Valence': 71, 'Length': 295, 'Acousticness': 0, 'Speechiness': 4, 'Popularity': 79}, {'title': 'Just the Way You Are', 'artist': 'Bruno Mars', 'genre': 'pop', 'year': 2010, 'BPM': 109, 'Energy': 84, 'Danceability': 64, 'Loudness': -5, 'Liveness': 9, 'Valence': 43, 'Length': 221, 'Acousticness': 2, 'Speechiness': 4, 'Popularity': 78}, {'title': 'Baby', 'artist': 'Justin Bieber', 'genre': 'canadian pop', 'year': 2010, 'BPM': 65, 'Energy': 86, 'Danceability': 73, 'Loudness': -5, 'Liveness': 11, 'Valence': 54, 'Length': 214, 'Acousticness': 4, 'Speechiness': 14, 'Popularity': 77}, {'title': 'Dynamite', 'artist': 'Taio Cruz', 'genre': 'dance pop', 'year': 2010, 'BPM': 120, 'Energy': 78, 'Danceability': 75, 'Loudness': -4, 'Liveness': 4, 'Valence': 82, 'Length': 203, 'Acousticness': 0, 'Speechiness': 9, 'Popularity': 77}, {'title': 'Secrets', 'artist': 'OneRepublic', 'genre': 'dance pop', 'year': 2010, 'BPM': 148, 'Energy': 76, 'Danceability': 52, 'Loudness': -6, 'Liveness': 12, 'Valence': 38, 'Length': 225, 'Acousticness': 7, 'Speechiness': 4, 'Popularity': 77}, {'title': 'Empire State of Mind (Part II) Broken Down', 'artist': 'Alicia Keys', 'genre': 'hip pop', 'year': 2010, 'BPM': 93, 'Energy': 37, 'Danceability': 48, 'Loudness': -8, 'Liveness': 12, 'Valence': 14, 'Length': 216, 'Acousticness': 74, 'Speechiness': 3, 'Popularity': 76}]
for i in range(len(playlist1)):
    print(playlist1[i]['title'])
    
print('')
    
sortedp = sort_playlist(playlist1, 'title')
for i in range(len(sortedp)):
    print(sortedp[i]['title'])
