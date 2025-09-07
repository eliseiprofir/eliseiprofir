import random


class Song:
    def __init__(self, title: str) -> None:
        self.title: str = title.title()
        self.next: Song | None = None
        self.prev: Song | None = None

    def __str__(self) -> str:
        before = self.prev.title if self.prev else None
        after = self.next.title if self.next else None
        return f"({before}<-) {self.title.upper()} (->{after})"

    def __repr__(self) -> str:
        before = self.prev.title if self.prev else None
        after = self.next.title if self.next else None
        return f"prev={before} - title={self.title} - next={after}"


class Playlist:
    def __init__(self) -> None:
        self.start: Song | None = None
        self.current: Song | None = None
        self.count: int = 0

    def add(self, title: str) -> None:
        self.count += 1
        new_song: Song = Song(title)
        if self.start is None:
            self.start = new_song
            return
        last_song: Song | None = self.start
        while last_song.next:
            last_song = last_song.next
        last_song.next = new_song
        new_song.prev = last_song

    def remove(self, title: str) -> None:
        title = title.title()
        current_song: Song | None = self.start
        if current_song and current_song.title == title:
            self.start = current_song.next
            if self.start is not None:
                self.start.prev = None
            # current_song = None
            self.count -= 1
            return

        while current_song and current_song.title != title:
            current_song = current_song.next

        if current_song is None:
            print(f"The song '{title}' was not found.")
            return
        if current_song.next:
            current_song.next.prev = current_song.prev
        if current_song.prev:
            current_song.prev.next = current_song.next
        self.count -= 1
        print(f"The song '{title}' was removed.")
        # current_song = None

    def search(self, title: str) -> str:
        title = title.title()
        current_song: Song = self.start
        index: int = 0
        while current_song:
            if current_song.title == title:
                return f"'{current_song.title}' found at index {index}."
            current_song = current_song.next
            index += 1
        return f"'{title}' was not found."

    def skip(self) -> None:
        if self.start is None:
            print("!! No songs in the playlist.")
            return
        if self.current is None:
            self.current = self.start
            print(f"| Starting playing the first song -- {self.current.title}")
            return
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"-> Skipping to -- {self.current.title}")
            return
        if self.current.next is None:
            print(f"! No more songs in the playlist. Playing the same song -- {self.current.title}")
            return

    def previous(self) -> None:
        if self.start is None:
            print("!! No songs in the playlist.")
            return
        if self.current is None:
            self.current = self.start
            print(f"No songs are playing. Playing the first song -- {self.current.title}")
            return
        if self.current.prev is None:
            print(f"! No more songs to go back. Playing the first song -- {self.current.title}")
            return
        if self.current.prev:
            self.current = self.current.prev
            print(f"<- Playing the previous song -- {self.current.title}")
            return

    def shuffle(self):
        playlist_songs = []
        current_song: Song | None = self.start
        if current_song is None:
            print("The playlist has no songs.")
        while current_song:
            playlist_songs.append(current_song.title)
            current_song = current_song.next
        random.shuffle(playlist_songs)
        return playlist_songs

    def length(self) -> str:
        return f"~ The playlist has {self.count} songs."

    def __str__(self) -> str:
        current_song: Song | None = self.start
        formatted: str = ""
        while current_song is not None:
            formatted += f"{str(current_song.title)}, "
            current_song = current_song.next
        formatted = formatted[:-2]
        return f"[{formatted}]"

    def __repr__(self) -> str:
        current_song: Song | None = self.start
        formatted: str = ""
        while current_song is not None:
            formatted += f"{str(current_song)}, "
            current_song = current_song.next
        formatted = formatted[:-2]
        return f"[{formatted}]"


playlist = Playlist()

print("Inserting...")
playlist.add("Falling in love")
playlist.add("Ave Maria")
playlist.add("Catch a Falling Star")
playlist.add("Caterina")
playlist.add("Christmas Eve")
print(playlist)
print(playlist.__repr__())
print()

print("Removing 'Caterina'...")
playlist.remove("Caterina")
print(playlist.length())
print(playlist)
print(playlist.__repr__())
print()

print("Searching...")
print(playlist.search("Caterina"))
print(playlist.search("ave maria"))
print()

print("Skipping & Previousing..")
playlist.skip()
playlist.skip()
playlist.skip()
playlist.skip()
playlist.skip()
playlist.previous()
playlist.previous()
playlist.previous()
playlist.previous()
print()

print("Shuffle playlist...")
print(playlist.shuffle())
print(playlist.shuffle())
print(playlist.shuffle())
