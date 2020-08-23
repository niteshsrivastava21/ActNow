import pymongo


class DbOperations:

    def insert_collection_data(self,list_to_insert, host_name, db_name, collection_name):
        db_client = pymongo.MongoClient(host_name)
        db_connection = db_client[db_name]
        db_collection = db_connection[collection_name]
        return_collection = db_collection.insert_many(list_to_insert)
        return return_collection

    def query_collection_data(self,query_dict,host_name,db_name,collection_name):
        db_client = pymongo.MongoClient(host_name)
        db_connection = db_client[db_name]
        db_collection = db_connection[collection_name]
        return_collection = db_collection.find(query_dict)
        return return_collection
