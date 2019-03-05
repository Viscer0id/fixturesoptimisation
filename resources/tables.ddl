create table rounds
(
	round integer,
	date text,
	day text
);

alter table rounds owner to postgres;

create table times
(
	day text,
	time text
);

alter table times owner to postgres;

create table rawdata
(
	default_age_group text,
	competition_name text,
	round_number integer,
	match_date text,
	match_day text,
	match_time text,
	club_1 text,
	team_1 text,
	club_2 text,
	team_2 text,
	venue_name text
);

alter table rawdata owner to postgres;

create table club
(
	clubname text,
	clubpk text,
	clubid integer,
	homevenuename text,
	homevenuepk text
);

alter table club owner to postgres;

create table competition
(
	competitionname text,
	competitionpk text,
	agegroup text,
	preferredday text,
	preferredtime text,
	weight integer
);

alter table competition owner to postgres;

create table team_competition
(
	competitionname text,
	competitionpk text,
	teamname text,
	teampk text
);

alter table team_competition owner to postgres;

create table team_club
(
	clubname text,
	teamname text,
	teampk text,
	clubpk text
);

alter table team_club owner to postgres;

create table venue
(
	venuename text,
	venuepk text,
	capacity integer
);

alter table venue owner to postgres;


-- All combinations of rounds (1 -> 15), days and times
create view all_rounds_datetimes as
select
      r.round, r.date, t.day, t.time
from
      rounds r, times t
where
      r.day = t.day
order by
      r.round, r.date, t.time;

-- All combinations of rounds (1 -> 15) days, times and venues
create view all_rounds_datetimes_venues as
select
      r.round, r.date, t.day, t.time, v.venuepk, v.capacity
from
      rounds r, times t, venue v
where
      r.day = t.day
order by
      r.round, r.date, t.time, v.venuepk;

-- All combinations of all teams and home venues for a competition, with preferred days, times and match weight
create view all_potential_matches as
with team1 as (
select
       competitionpk
       ,teampk
from
     team_competition
  ),
team2 as (
select
       competitionpk
       ,teampk
from
     team_competition
     )
select
      team1.competitionpk
     ,team1.teampk home_teampk
     ,team2.teampk away_teampk
     ,v.venuepk home_venuepk
     ,c.preferredday
     ,c.preferredtime
     ,c.weight
from
      team1 cross join team2
      join competition c on team1.competitionpk = c.competitionpk
      join team_club tc on team1.teampk = tc.teampk
      join club on tc.clubpk = club.clubpk
      join venue v on club.homevenuepk = v.venuepk
where
      team1.teampk <> team2.teampk
      and team1.competitionpk = team2.competitionpk
order by
      c.competitionpk, home_teampk;
