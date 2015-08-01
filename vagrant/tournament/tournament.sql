-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- --------------------------------------------------------------------------------------------

-- Comment out the following lines to prevent dropping the tournament database, tables, and views if they exist before being created:
DROP DATABASE IF EXISTS tournament;
DROP TABLE IF EXISTS players CASCADE;
DROP TABLE IF EXISTS matches CASCADE;
DROP VIEW IF EXISTS standings CASCADE;
-- By default everything is dropped and the program will start from scratch.

-- Create tournament database and connect to it
CREATE DATABASE tournament;
\connect tournament

-- Create player table
CREATE TABLE players(
  p_id SERIAL PRIMARY KEY,
  p_name TEXT NOT NULL
);

-- Creates matches table
CREATE TABLE matches (
  m_id serial PRIMARY KEY,
  win INTEGER,
  lose INTEGER,
  FOREIGN KEY(win) REFERENCES players(p_id),
  FOREIGN KEY(lose) REFERENCES players(p_id)
);

-- Creates a view of matches played sorted by won count
CREATE VIEW standings AS
SELECT players.p_id as p_id, players.p_name,
(SELECT count(*) FROM matches WHERE matches.win = players.p_id) as won,
(SELECT count(*) FROM matches WHERE players.p_id in (win, lose)) as played
FROM players GROUP BY players.p_id ORDER BY won DESC;