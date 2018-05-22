from decouple import config


# Tells browser to cache static for a long time
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME =  config('AWS_STORAGE_BUCKET_NAME', default="") #'static4toufikswar'
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default="") #'eu-west-3'
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default="") #'AKIAIHBMPVBC7RAUYVVA'
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default="") #'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'

# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME



# Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# you run `collectstatic`).
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


STATICFILES_LOCATION = config('STATICFILES_LOCATION', default="static")
STATICFILES_STORAGE = config('STATICFILES_STORAGE', default="")

MEDIAFILES_LOCATION = config('MEDIAFILES_LOCATION', default="media")
DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE', default="")

