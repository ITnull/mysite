# mysite

----------------------
项目：django项目
作者：柯善武
日期：20180802

---------------------

1. 配置数据库
/mysite/mysite/settings.py

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'swkedb',
        'USER': 'root',
        'PASSWORD':'360481',
        'HOST': 'localhost',
        'PORT':'', 
    }
}

2.
