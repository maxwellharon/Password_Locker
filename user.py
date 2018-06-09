class User:
    '''
    This is a class that generates new instances for the user in question
    '''
    user_list = []

    def __init__(self,login_name,password):
        '''
        This method defines properties for our user object
        '''
        self.login_name = login_name
        self.password = password


    def save_user(self):
        '''
        This is a method which allows the user to save input
        '''

        User.user_list.append(self)

    @classmethod
    def user_login (cls, login):
        '''
        This is a method in which a user can check his/her credentials
        '''
        for User in cls.user_list:
            if User.login_name == login:
                return User
