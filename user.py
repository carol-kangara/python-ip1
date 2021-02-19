class Users:
    """
    class that generates new instances of users
    """
    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass 
    def __init__(self,user_name,password):
        self.user_name=user_name
        self.password=password
    def save-user(self): 
        #used to add or to save instances of user to the user list