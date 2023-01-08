import psycopg2.pool

# Create a connection pool
conn_pool = psycopg2.pool.ThreadedConnectionPool(
    minconn=3,
    maxconn=5,
    host='localhost',
    database='gamesdb',
    user='postgres',
    password='mypassword',
    port=5432
)

def fetch_games():
    try:
        # Get a connection from the pool
        conn = conn_pool.getconn()
        cur = conn.cursor()

        # Execute the SELECT query
        cur.execute("SELECT * FROM games")

        # Fetch the rows from the cursor
        rows = cur.fetchall()

        # Build the list of games from the rows
        games = [
            {
                'id': row[0],
                'title': row[1],
                'genre': row[2],
                'played': row[3]
            }
            for row in rows
        ]

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching games:", error)
        games = []

    finally:
        # Return the connection to the pool
        if cur:
            cur.close()
        if conn:
            conn_pool.putconn(conn)

    return games

def add_game(id,title, genre, played):
    try:
        # Get a connection from the pool
        conn = conn_pool.getconn()
        cur = conn.cursor()

        # Execute the INSERT query
        cur.execute("INSERT INTO games (id, title, genre, played) VALUES (%s, %s, %s, %s)", (id, title, genre, played))

        # Commit the transaction
        conn.commit()

        success = True

    except (Exception, psycopg2.Error) as error:
        print("Error while adding game:", error)
        success = False

    finally:
        # Return the connection to the pool
        if cur:
            cur.close()
        if conn:
            conn_pool.putconn(conn)

    return success

def update_game(game_id, title, genre, played):
    try:
        # Get a connection from the pool
        conn = conn_pool.getconn()
        cur = conn.cursor()

        # Execute the UPDATE query
        cur.execute("UPDATE games SET title=%s, genre=%s, played=%s WHERE id=%s", (title, genre, played, game_id))

        # Commit the transaction
        conn.commit()

        success = True

    except (Exception, psycopg2.Error) as error:
        print("Error while updating game:", error)
        success = False

    finally:
        # Return the connection to the pool
        if cur:
            cur.close()
        if conn:
            conn_pool.putconn(conn)

    return success

def delete_game(game_id):
    try:
        # Get a connection from the pool
        conn = conn_pool.getconn()
        cur = conn.cursor()

        # Execute the DELETE query
        cur.execute("DELETE FROM games WHERE id=%s", (game_id,))

        # Commit the transaction
        conn.commit()

        success = True

    except (Exception, psycopg2.Error) as error:
        print("Error while deleting game:", error)
        success = False

    finally:
        # Return the connection to the pool
        if cur:
            cur.close()
        if conn:
            conn_pool.putconn(conn)

    return success
