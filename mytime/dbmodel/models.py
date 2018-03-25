from django.db import models

import logging
# Create your models here.

logger = logging.getLogger(__name__)

class BaseDao(object):
    def __init__(self, object_model):
        self.model = object_model

    def get(self, cond):
        result = None
        try:
            result = self.model.objects.get(cond)
        except Exception:
            logger.error('BaseDao.get ')
    
