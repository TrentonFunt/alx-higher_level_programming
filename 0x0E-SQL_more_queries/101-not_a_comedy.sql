-- Retrieve the ID of the "Comedy" genre
SELECT id
FROM tv_genres
WHERE name = 'Comedy';

-- List all shows without the genre "Comedy"
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
   OR tv_show_genres.genre_id NOT IN (
       SELECT id
       FROM tv_genres
       WHERE name = 'Comedy'
   )
ORDER BY tv_shows.title ASC;
