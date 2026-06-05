import psycopg2


def get_connection():

    return psycopg2.connect(
        host="localhost",
        database="rent_dashboard",
        user="davod2x"
    )