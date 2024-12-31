from model.autor import Autor
from view.crud import menu_crud
from view.create import menu_create
from view.delete import menu_delete
from view.edit import menu_edit
from view.search import menu_search


class AutorController():
    @staticmethod
    def index()->None:
        menu_crud('Autor', AutorController)
    
    @staticmethod    
    def show(id: str)->dict:
        autor = Autor() 
        data_autor = autor.get_id(id)
        return data_autor
    
    @staticmethod
    def edit():
        list_parameters = ['name', 'nacionality']
        menu_edit('Autor', AutorController, list_parameters)
    
    @staticmethod
    def store(id: str, name: str, nacionality: str):
        autor = Autor()
        autor.save(id,name,nacionality)
    
    @staticmethod
    def create():
        list_parameters = ['id','name', 'nacionality']
        menu_create('Autor', AutorController, list_parameters)
    
    @staticmethod
    def update(id: str, name = None, nacionality = None)-> bool:
        autor = Autor()        
        data_autor = autor.get_id(id)        
        if data_autor is None:
            return False      
        autor.update(id, name, nacionality)
        return True
    
    @staticmethod
    def delete():
        menu_delete('Autor', AutorController)
    
    @staticmethod
    def destroy(id: str):
        autor = Autor()
        autor.delete(id)
    
    @staticmethod
    def search(name_find: str):
        autor = Autor()
        list_autor = autor.search(name_find)
        return list_autor
    
    @staticmethod
    def search_IU():
        menu_search('Autor', AutorController)