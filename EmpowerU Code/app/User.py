import os
class User():
    @staticmethod
    def authenticate(input_username,input_password,path):
        delimiter = ","
        if os.path.exists(path):
            with open(path,"r") as rp:
                lines = rp.readlines()
            for line in lines:
                user_id,first_name,last_name,contact_num,username,password,code = line.strip().split(delimiter)
                if input_username == username and input_password == password:
                    return User(user_id,first_name,last_name,username,password,code)
            else:
                return None
        else:
            print(f"Please check subdirectory and file {path} exists.")

    def __init__(self,user_id,first_name,last_name,username,password,code):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.code = code
    
    
if __name__ == "__main__":
    pass
