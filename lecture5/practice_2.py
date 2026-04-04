class Song:
    def __init__(self, title, artist, durations):
        self.title = title
        self.artist = artist
        self.duration_in_seconds = durations
    def play(self):
        print(f"Playing: {self.title} by {self.artist} .")
    
s1 = Song("Song A", "Artist X", 180)
s2 = Song("Song B", "Artist Y", 210)
s3 = Song("Song C", "Artist Z", 195)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self,song):
        self.songs.append(song)
        print(f"{song.title} added successfully...")
    def remove_song(self, title):
        for i, song in enumerate(self.songs):  
            if song.title == title:
                del self.songs[i] 
                print(f"Removed {title} from {self.name}")
                return 
        print(f"{title} not found in {self.name}") 
    def play_all(self):
        for song in self.songs:
            song.play()
    def total_durations(self):
        total = 0
        for song in self.songs:
            total += song.duration_in_seconds 
        return total 
workout = Playlist("Gym Energy")
workout.add_song(s1), workout.add_song(s2)
chill = Playlist("Relax")
chill.add_song(s2), chill.add_song(s3)
workout.play_all()
workout.add_song(s1) 
workout.remove_song("Song A")  
workout.remove_song("Ghost")  
print(workout.total_durations())
s2.title = "TEST MUTATION"
chill.play_all()