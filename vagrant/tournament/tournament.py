#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM matches")
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players")
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM players")
    p_count = cursor.fetchone()[0]
    conn.close()
    return p_count

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO players (p_name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
	# The If statement reorders the results by wins/games played if wins > 0 and also equal.
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM standings;")
    results = cursor.fetchall()
    if (results[0][2] != 0) and (results[0][2] == results[1][2]):
        cursor.execute("SELECT p_id, p_name, won, played FROM standings ORDER BY (cast(won AS DECIMAL)/played) DESC;")
        results = cursor.fetchall()
    conn.close()
    return results


def reportMatch(win, lose):
    """Records the outcome of a single match between two players.
    Args:
      win:  the id number of the player who won
      lose:  the id number of the player who lost
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO matches (win, lose) VALUES (%s, %s)", (win, lose,))
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM standings")
    results = cursor.fetchall()
    pairs = []
    count = len(results)
    for a in range(0, count - 1, 2):
        pairs_list = (results[a][0],results[a][1],results[a + 1][0],results[a + 1][1])
        pairs.append(pairs_list)
    conn.close()
    return pairs