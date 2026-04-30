# from abc import ABC, abstractmethod

# class MediaFile(ABC):
#     def __init__(self, name):
#         self.name = name
    
#     @property
#     @abstractmethod
#     def file_type(self):
#         pass
#     @abstractmethod
#     def process(self):
#         pass

#     def __add__(self, other):
#         """Operator Overloading: Combining two media files creates a Playlist."""
#         if isinstance(other, (MediaFile, CloudLink)):
#             return Playlist([self, other])
#         return NotImplemented

# class VideoFile(MediaFile):
#     @property
#     def file_type(self):
#         return "Video"
    
#     def process(self):
#         print(f"[{self.name}] Decoding H.264 streams and optimizing frames...")
# class AudioFile(MediaFile):
#     @property
#     def file_type(self):
#         return "Audio"
    
#     def process(self):
#         print(f"[{self.name}] Normalizing decibels and checking sample rates...")

# class CloudLink:
#     def __init__(self, url):
#         self.file_type = "Cloud strems"
#         self.name = url
    
#     def process(self):
#         print(f"[{self.name}] Buffering external stream from remote server...")

# class Playlist:
#     def __init__(self, items):
#         self.items = items

#     def process(self):
#         print(f"--- Processing Playlist ({len(self.items)} items) ---")
#         for item in self.items:
#             item.process()

# def runing_batch_processing(files):
#     print("Starting Batch Media Conversion...")
#     for file in files:
#         file.process()
#     print("Converstion Complete\n")


# if __name__ == "__main__":
#     video = VideoFile("Cinematic_Intro.mp4")
#     audio = AudioFile("Background_Music.wav")
#     link = CloudLink("https://cloud-storage.com/clip_01")

#     media_queue = [video, audio, link]
#     runing_batch_processing(media_queue)
#     print("Combining Video and Audio into a Playlist...")
#     my_playlist = video + audio 
#     my_playlist.process()

class X:
    print("inside Class X")
class Y:
    print("inside Class Y")
class A(X, Y):
    print("inside Class A")
class B(Y, X):
    print("inside Class B")
# This next line will CRASH Python:
class C(A, B):
    print("inside Class C")
# TypeError: Cannot create a consistent method resolution order (MRO)

c = C()
print(c)