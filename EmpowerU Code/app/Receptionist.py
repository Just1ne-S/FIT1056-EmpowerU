import os
from app.User import User

class Receptionist(User):
    @staticmethod
    def authenticate(input_username,input_password,path):
        delimiter = ","
        if os.path.exists(path):
            with open(path,"r") as rp:
                lines = rp.readlines()
            for line in lines:
                user_id,first_name,last_name,contact_num,username,password = line.strip().split(delimiter)
                if input_username == username and input_password == password:
                    return Receptionist(user_id,first_name,last_name,username,password)
            else:
                return None
        else:
            print(f"Please check subdirectory and file {path} exists.")

    def __init__(self,user_id,first_name,last_name,username,password):
        super().__init__(user_id,first_name,last_name,username,password)

if __name__ == "__main__":
    pass
