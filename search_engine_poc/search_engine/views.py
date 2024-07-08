# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Database connection details (adjust these according to your setup)
db_host = 'localhost'
db_port = '5432'
db_name = 'australia'
db_user = 'postgres'
db_password = 'Login@#6009'

def search_trademarks(request):
    if request.method == 'GET' and 'keyword' in request.GET:
        keyword = request.GET['keyword']

        try:
            with psycopg2.connect(
                host=db_host,
                port=db_port,
                dbname=db_name,
                user=db_user,
                password=db_password
            ) as conn:
                with conn.cursor() as cur:
                    query = """
                    SELECT * FROM trademarks
                    WHERE verbalElements ILIKE %s
                    """
                    cur.execute(query, ('%' + keyword + '%',))
                    results = cur.fetchall()

            context = {
                'results': results,
                'keyword': keyword
            }
            return render(request, 'search_results.html', context)

        except psycopg2.Error as e:
            error_message = f'Error fetching data from database: {e}'
            return HttpResponse(error_message)

    return render(request, 'search_form.html')
