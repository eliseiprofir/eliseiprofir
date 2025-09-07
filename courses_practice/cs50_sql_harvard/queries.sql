-- See the songs ordered by how many times they were played
SELECT * FROM "songs"
ORDER BY "play_count" DESC;

-- See the favourite songs using the view I created
SELECT * FROM "favourite_songs"
ORDER BY "play_count" DESC;

-- See all the songs played by Kenny G
SELECT "songs"."title" FROM "songs"
JOIN "artists" ON "artist_songs"."artist_id" = "artists"."id"
JOIN "artist_songs" ON "artist_songs"."song_id" = "songs"."id"
WHERE "artists"."name" = 'Kenny G';

-- See all the artists and how many songs they have
SELECT "artists"."name", COUNT("songs"."title") as 'no_of_songs' FROM "artists"
JOIN "artist_songs" ON "artist_songs"."artist_id" = "artists"."id"
JOIN "songs" ON "artist_songs"."song_id" = "songs"."id"
GROUP BY "artists"."name";

-- See the artists who has the most played songs
SELECT "artists"."name", SUM("songs"."play_count") AS 'no_of_play_count' FROM "artists"
JOIN "artist_songs" ON "artist_songs"."artist_id" = "artists"."id"
JOIN "songs" ON "artist_songs"."song_id" = "songs"."id"
GROUP BY "artists"."name"
ORDER BY SUM("songs"."play_count") DESC;
