import json
from bson import ObjectId
import pymongo

class Crud:

    def __init__(self, database):
        self.database = database

###############################################Get All Data######################################################
    async def getAllData(self, collection_name):
        collection = self.database[collection_name]
        try:
            items = []
            async for item in collection.find({}):
                item["_id"] = str(item["_id"])
                items.append(item)
            if len(items) > 0:
                result = {"status" : "success" , "message":"Research Successfully", "data" : items}
            else:
                result = {"status" : "failure" , "message":"Items Not Found", "data" : None}
            return items
        except pymongo.errors.PyMongoError as e:
            result =  {"status" : "failure" , "message":f"Erreur lors de la récupération de l'élément : {e}", "data" : None}
        finally:
            return result

###############################################Get Item By Id######################################################
    async def getOneById(self, collection_name, item_id):
        collection = self.database[collection_name]
        try:
            item = await collection.find_one({"_id": ObjectId(item_id)})
            if item:
                item["_id"] = str(item["_id"])
                result = {"status" : "success" , "message":"Research Successfully", "data" : item}
            else:
                result = {"status" : "failure" , "message":"Item Not Found", "data" : None}
        except pymongo.errors.PyMongoError as e:
            result =  {"status" : "failure" , "message":f"Erreur lors de la récupération de l'élément : {e}", "data" : None}
        finally:
            return result

###############################################Insert One Item######################################################
    async def insertOne(self, collection_name,item):
        collection = self.database[collection_name]
        try:
            result = await collection.insert_one(item)
            if result.inserted_id:
                item["_id"] = str(result.inserted_id)
                result = {"status" : "success" , "message":"Insertion Successfully", "data" : item}
            else:
                result = {"status" : "failure" , "message":"Insertion Failed", "data" : None}
        except pymongo.errors.PyMongoError as e:
            result =  {"status" : "failure" , "message":f"Erreur lors de la récupération de l'élément : {e}", "data" : None}
        finally:
            return result

###############################################Update One Item######################################################
    async def updateOneById(self, collection_name, item_id, new_data):
        collection = self.database[collection_name]
        try:
            result = await collection.update_one({"_id": ObjectId(item_id)}, {"$set": new_data})
            if result.modified_count > 0:
                updated_item = await collection.find_one({"_id": ObjectId(item_id)})
                updated_item['_id'] = str(ObjectId(updated_item['_id']))
                result =  {"status" : "success" , "message":"Updated Successfully", "data" : updated_item}
            else:
                result =  {"status" : "failure" ,"message":"Updated Failed", "data" : None}
        except pymongo.errors.PyMongoError as e:
            result =  {"status" : "failure" ,"message":f"Erreur lors de la mise à jour de l'élément : {e}", "data" : None}
        finally:
            return result

###############################################Delete One Item######################################################
    async def deleteOneById(self, collection_name, item_id):
        collection = self.database[collection_name]
        try:
            isDeleted = await collection.delete_one({"_id": ObjectId(item_id)})
            if isDeleted.deleted_count > 0:
                result = {"status": "success", "message": "Deleted Successfully", "data": None}
            else:
                result = {"status": "failure", "message": "Delete Failed", "data": None}
        except pymongo.errors.PyMongoError as e:
            result = {"status": "failure", "message": f"Erreur lors de la suppression de l'élément : {e}", "data": None}
        finally:
            return result


