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
    
songs = read_dataset('spotify-dataset.csv')
print(songs)
