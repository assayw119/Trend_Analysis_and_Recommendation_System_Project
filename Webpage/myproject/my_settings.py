
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'capston',
        'USER' : 'root',
        'PASSWORD' : 'qwedsa2249',
        'HOST' : 'localhost',
        'PORT' : '3306',
        'OPTIONS' : {"charset": "utf8mb4"},
    }
}

SECRET_KEY = 'django-insecure-grf(o(q-((y4sm1k8q^-qjza+18pmx8=s5=k=pq3^d!p*@f#=j'
