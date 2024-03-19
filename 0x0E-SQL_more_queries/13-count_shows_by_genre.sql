-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- shows linked to each.
-- Does not display genres without linked shows.
-- Records are ordered by descending number of shows linked.
SELECT g.`name` AS `genre`,
       COUNT(t.`show_id`) AS `number_of_shows`
  FROM `tv_show_genres` AS t
       INNER JOIN `tv_genres` AS g
       ON t.`genre_id` = g.`id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
