import configparser

from model.DbOperations import DbOperations


def get_config_data(parent_tag, child_tag):
    config = configparser.ConfigParser()
    config.read("../config.ini")
    value_to_return = config[parent_tag][child_tag]
    return value_to_return


host_name = get_config_data("db_params", "db_host")
db_name = get_config_data("db_params", "db_name")
db_collection = get_config_data("db_params", "db_user_collection")
# dict_insert={
#     "name": "jiesh",
#     "age":57
# }
# list_to_insert= [dict_insert]
dbOp = DbOperations()
# dbOp.insert_collection_data(list_to_insert,host_name,db_name,db_collection)
result = dbOp.query_collection_data({"age": {$gt: 30}}, host_name, db_name, db_collection)
for x in result:
    print(x["name"])
