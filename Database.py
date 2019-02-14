from pymongo import MongoClient
from pymongo.errors import *
import json
import bson.json_util as bson
from Message import MessageJson
client = MongoClient('localhost', 27017)
mongo = client.oasis


class Data():

  def find(self, datas):
      findItems = mongo.ranking.find(
          datas,
          {'_id': 0}
      ).sort([('rate', -1), ('date', 1)])
      return bson.dumps(findItems, ensure_ascii=False)

  def insert(self, datas):
      result = mongo.ranking.insert(datas)
      return MessageJson.INSERT_SUCCESS.value if result is not None else MessageJson.INSERT_FAILED.value

  def delete(self, datas):
      result = mongo.ranking.remove(datas)
      return MessageJson.DELETE_SUCCESS.value if result['n'] > 0 else MessageJson.DELETE_SUCCESS.value
