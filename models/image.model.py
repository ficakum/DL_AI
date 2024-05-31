from mongoengine import *
import sys
sys.path.append('../')
from constants.constant import ModelConstants

class Image (Document):
  meta={'collection': ModelConstants["IMAGE"], 'strict': False}

  featureVector = StringField(required=True)
  product = ReferenceField("product")