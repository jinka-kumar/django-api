from django.conf import settings

class Database:
    db = settings.db
    collection = db['film_crew']