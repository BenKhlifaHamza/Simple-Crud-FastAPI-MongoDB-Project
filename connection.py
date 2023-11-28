from motor.motor_asyncio import AsyncIOMotorClient
class MyConnection : 
    
    def __init__(self , server_url="server_url", db_name = "db_name") :
        self.server_url = server_url
        self.db_name = db_name
        
    def getConnection(self) :
        try:
            client = AsyncIOMotorClient(self.server_url)
            return client[self.db_name]
        except Exception as e:
            print(f"Erreur de connexion à MongoDB : {e}")
            return None