import pyperclip
import random

class Credentials:
    '''
    This is a class that generates the credentials of the user in question
    '''
    credentials_list = []
    user_password_list = []


    def __init__(self, account_name, user_name, email, password):
        '''
        This is a method that helps us define the properties of the users credentials
        '''
        self.account_name = account_name
        self.user_name = user_name
        self.email = email
        self.password = password

    def save_credentials(self):
        '''
        save_credentials method save credentials object into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_contact method deletes an object from the credentials_list
        '''
        Credentials.credentials_list.remove(self)
