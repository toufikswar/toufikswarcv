from django.conf import settings
from mycv.aws.conf import *
from storages.backends.s3boto3 import S3Boto3Storage



class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    def _normalize_name(self, name):
  
        return self.location + '/' + name
    

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

