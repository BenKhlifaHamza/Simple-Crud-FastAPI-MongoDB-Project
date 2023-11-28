from fastapi import FastAPI
from connection import MyConnection
from crud import Crud
from model import User
app = FastAPI()

#-------------------------Pour Tester A Partir De Postman-------------------------#
myConnection = MyConnection(server_url="mongodb://localhost:27017" , db_name="blog")
myDatabase = myConnection.getConnection()
crud = Crud(database=myDatabase)

@app.get("/users/")
async def get_all_users():
    all_users = await crud.getAllData("users")
    return all_users

@app.get("/users/{user_id}")
async def get_one_user(user_id: str):
    user = await crud.getOneById(collection_name="users", item_id=user_id)
    return user

@app.post("/adduser/")
async def create_user(user: User):
    user_dict = dict(user)# Création d'un dictionnaire à partir du modèle User
    result = await crud.insertOne("users" ,user_dict)# Insertion de l'utilisateur dans la collection MongoDB
    return result

@app.patch("/updateuser/{user_id}")
async def update_user(user_id : str , new_data: dict):
    result = await crud.updateOneById("users", user_id,new_data)
    return result

@app.delete("/deleteuser/{user_id}")
async def delete_user(user_id):
    result = await crud.deleteOneById("users",user_id)
    return result

#-------------------------Pour Tester A Partir De Navigateur-------------------------#
# myConnection = MyConnection(server_url="mongodb://localhost:27017" , db_name="blog")
# myDatabase = myConnection.getConnection()
# crud = Crud(database=myDatabase)

# @app.get("/users/")
# async def get_all_users():
#     all_users = await crud.getAllData(collection_name="users")
#     return all_users

# @app.get("/users/{user_id}")
# async def get_one_user(user_id: str):
#     user = await crud.getOneById(collection_name="users", item_id=user_id)
#     return user

# @app.get("/adduser/")
# async def add_user():
#     user = {"name":"Samia","age":55,"city":"Monastir"}
#     result = await crud.insertOne(collection_name="users",item=user)
#     return result

# @app.get("/updateuser/{user_id}")
# async def update_user(user_id):
#     new_user_data = {"age": 35}
#     result = await crud.updateOneById(collection_name="users", item_id=user_id, new_data=new_user_data)
#     return result

# @app.get("/deleteuser/{user_id}")
# async def delete_user(user_id):
#     result = await crud.deleteOneById(collection_name="users", item_id=user_id)
#     return result

