import psycopg2

# Database connection details (adjust these according to your setup)
db_host = 'localhost'
db_port = '5432'
db_name = 'australia'
db_user = 'postgres'
db_password = 'Login@#6009'

# Connect to PostgreSQL
try:
    with psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    ) as conn:
        with conn.cursor() as cur:
            # SEARCH BASED ON VERBAL_ELEMENT
            def search_trademarks(keyword):
                query = """
                SELECT * FROM trademarks
                WHERE verbalElements ILIKE %s
                """
                cur.execute(query, ('%' + keyword + '%',))
                results = cur.fetchall()
                return results

            # Example search
            keyword = 'Romaus Studios'
            results = search_trademarks(keyword)
            # for result in results:
            print(results)

except psycopg2.Error as e:
    print(f'Error connecting to database: {e}')
