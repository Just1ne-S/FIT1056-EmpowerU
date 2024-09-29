import os
class User():
    @staticmethod
    def authenticate(input_username,input_password):
        path = "./data/login_info.txt"
        delimiter = ","
        if os.path.exists(path):
            with open(path,"r") as rp:
                lines = rp.readlines()
            for line in lines:
                first_name,last_name,contact_num,username,password = line.split(delimiter)
            if input_username == username and input_password == password:
                return User(first_name,last_name,username,password)
            else:
                return None
        else:
            print(f"Please check subdirectory and file {path} exists.")

    def __init__(self,first_name,last_name,username,password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
    
    
if __name__ == "__main__":
    pass
