class User:
    '''
    This is a class that generates new instances for the user in question
    '''
    def __init__(self,login_name,password):
        '''
        This method defines properties for our user object
        '''
        self.login_name = login_name
        self.password = password
