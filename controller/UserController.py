from model.user import User
from view.crud import menu_crud
from view.create import menu_create
from view.delete import menu_delete
from view.edit import menu_edit
from view.search import menu_search


class UserController():
    @staticmethod
    def index()->None:
        menu_crud('User', UserController)
    
    @staticmethod    
    def show(id: str)->dict:
        user = User() 
        data_user = user.get_id(id)
        return data_user
    
    @staticmethod
    def edit():
        list_parameters = ['name', 'age']
        menu_edit('User', UserController, list_parameters)
    
    @staticmethod
    def store(id: str, name: str, age: int):
        user = User()
        user.save(id,name,age)
    
    @staticmethod
    def create():
        list_parameters = ['id','name', 'age']
        menu_create('User', UserController, list_parameters)
    
    @staticmethod
    def update(id: str, name = None, age = None)-> bool:
        user = User()        
        data_user = user.get_id(id)        
        if data_user is None:
            return False      
        user.update(id, name, age)
        return True
    
    @staticmethod
    def delete():
        menu_delete('User', UserController)
    
    @staticmethod
    def destroy(id: str):
        user = User()
        user.delete(id)
    
    @staticmethod
    def search(name_find: str):
        user = User()
        list_user = user.search(name_find)
        return list_user
    
    @staticmethod
    def search_IU():
        menu_search('User', UserController)