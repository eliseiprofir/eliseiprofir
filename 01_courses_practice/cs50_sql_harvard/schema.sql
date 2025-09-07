-- Represent all the songs in the library
CREATE TABLE "songs" (
    "id" INTEGER NOT NULL UNIQUE,
    "title" TEXT NOT NULL,
    "year" INTEGER,
    "play_count" INTEGER DEFAULT 0,
    "favourite" TEXT CHECK ("favourite" IN ('yes', 'no')) DEFAULT 'no',
    PRIMARY KEY("id")
);

-- Represent all the albums
CREATE TABLE "albums" (
    "id" INTEGER NOT NULL UNIQUE,
    "title" TEXT NOT NULL,
    "artist" TEXT,
    "year" INTEGER,
    PRIMARY KEY("id")
);

-- Represent all the artists
CREATE TABLE "artists" (
    "id" INTEGER NOT NULL UNIQUE,
    "name" TEXT NOT NULL,
    PRIMARY KEY("id")
);

-- Represent the relation between albums and songs
CREATE TABLE "album_songs" (
    "song_id" INT NOT NULL,
    "album_id" INT NOT NULL,
    PRIMARY KEY("song_id", "album_id"),
    FOREIGN KEY("song_id") REFERENCES "songs"("id") ON DELETE CASCADE,
    FOREIGN KEY("album_id") REFERENCES "albums"("id") ON DELETE CASCADE
);

-- Represent the relation between artists and songs
CREATE TABLE "artist_songs" (
    "song_id" INT NOT NULL,
    "artist_id" INT NOT NULL,
    PRIMARY KEY("song_id", "artist_id"),
    FOREIGN KEY("song_id") REFERENCES "songs"("id") ON DELETE CASCADE,
    FOREIGN KEY("artist_id") REFERENCES "artists"("id") ON DELETE CASCADE
);

-- Represent the relation between artists and albums
CREATE TABLE "artist_albums" (
    "album_id" INT NOT NULL,
    "artist_id" INT NOT NULL,
    PRIMARY KEY("album_id", "artist_id"),
    FOREIGN KEY("album_id") REFERENCES "albums"("id") ON DELETE CASCADE,
    FOREIGN KEY("artist_id") REFERENCES "artists"("id") ON DELETE CASCADE
);

-- Create indexes to speed common searches
CREATE INDEX "songs_index" ON "songs" ("id", "title");
CREATE INDEX "albums_index" ON "albums" ("title");
CREATE INDEX "artists_index" ON "artists" ("name");

-- Create view for favourite songs
CREATE VIEW "favourite_songs" AS
SELECT * FROM "songs"
WHERE "favourite" = 'yes';

-- Create entries for songs table
INSERT INTO "songs" ("id", "title", "year", "play_count", "favourite") VALUES
(1, 'Feeling Good', 2005, 3, 'yes'),
(2, 'Home', 2005, 4, 'no'),
(3, 'Catch a Falling Star', 1957, 7, 'no'),
(4, 'Magic Moments', 1957, 9, 'yes'),
(5, 'He Touched Me', 1996, 8, 'no'),
(6, 'Yes, I Know!', 1997, 5, 'yes'),
(7, 'La Serenissima', 1981, 1, 'yes'),
(8, 'Breathless', 1992, 0, 'no'),
(9, 'The Shadow of Your Smile', 1965, 1, 'yes'),
(10, 'Songbird', 1986, 2, 'no');

-- Create entries for albums table
INSERT INTO "albums" ("id", "title", "artist", "year") VALUES
(1, 'It’s Time', 'Michael Bublé', 2005),
(2, 'Crazy Love', 'Michael Bublé', 2009),
(3, 'Perry Como Sings Just For You', 'Perry Como', 1958),
(4, 'The Best of Perry Como', 'Perry Como', 1975),
(5, 'Back Home in Indiana', 'Gaither Vocal Band', 1997),
(6, 'Southern Classics', 'Gaither Vocal Band', 1996),
(7, 'La Serenissima', 'Rondo Veneziano', 1981),
(8, 'Venice in Peril', 'Rondo Veneziano', 1984),
(9, 'Breathless', 'Kenny G', 1992),
(10, 'Silhouette', 'Kenny G', 1988);

-- Create entries for artists table
INSERT INTO "artists" ("id", "name") VALUES
(1, 'Michael Bublé'),
(2, 'Perry Como'),
(3, 'Gaither Vocal Band'),
(4, 'Rondo Veneziano'),
(5, 'Kenny G');

-- Create entries for album_songs relational table
INSERT INTO "album_songs" ("song_id", "album_id") VALUES
(1, 1),
(2, 1),
(3, 3),
(4, 3),
(5, 5),
(6, 5),
(7, 7),
(8, 7),
(9, 9),
(10, 9);

-- Create entries for artist_songs relational table
INSERT INTO "artist_songs" ("song_id", "artist_id") VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 3),
(6, 3),
(7, 4),
(8, 4),
(9, 5),
(10, 5);

-- Create entries for artist_albums relational table
INSERT INTO "artist_albums" ("album_id", "artist_id") VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 3),
(6, 3),
(7, 4),
(8, 4),
(9, 5),
(10, 5);
