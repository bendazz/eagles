select week,
       yards_gained,
       sum(yards_gained) over (partition by week order by game_seconds_remaining desc) as cumulative_yards,
       60 - game_seconds_remaining/60 as minutes_elapsed,
       CASE 
           WHEN away_team = 'PHI' THEN home_team 
           ELSE away_team 
       END as opponent,
       team_logo_espn,team_name,
       CASE 
           WHEN away_team = 'PHI' THEN 'away' 
           ELSE 'home'
       END as away_home,
       home_score,away_score
from eagles inner join teams on (CASE WHEN away_team = 'PHI' THEN home_team ELSE away_team END) = teams.team_abbr
where play_type = 'pass' and sack = 0 and passer_player_id = '00-0036389'