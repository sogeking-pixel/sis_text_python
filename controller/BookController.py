from model.book import Book
from model.autor import Autor
from view.crud import menu_crud
from view.create import menu_create
from view.delete import menu_delete
from view.edit import menu_edit
from view.search import menu_search


class BookController():
    @staticmethod
    def index()->None:
        menu_crud('book', BookController)
    
    @staticmethod    
    def show(id: str)->dict:
        book = Book() 
        data_book = book.get_id(id)
        return data_book
    
    @staticmethod
    def edit():
        list_parameters = ['title', 'cant_page','date_created','id_autor']
        menu_edit('Libro', BookController, list_parameters)
    
    @staticmethod
    def store(id: str, title: str, cant_page: str, date_created: str, id_autor: str):
        autor = Autor()
        if autor.get_id(id_autor) is None:
            return False
        book = Book()
        book.save(id,title,int(cant_page),date_created,id_autor)
    
    @staticmethod
    def create():
        list_parameters = ['id','title', 'cant_page','date_created','id_autor']
        menu_create('Libro', BookController, list_parameters)
    
    @staticmethod
    def update(id: str, title = None, cant_page = None, date_created = None, id_autor = None )-> bool:
        autor = Autor()
        if autor.get_id(id_autor) is None:
            return False        
        book = Book()        
        data_book = book.get_id(id)        
        if data_book is None:
            return False
        if cant_page is not None:
            cant_page = int(cant_page)      
        book.update(id,title,cant_page,date_created,id_autor)
        return True
    
    @staticmethod
    def delete():
        menu_delete('Libro', BookController)
    
    @staticmethod
    def destroy(id: str):
        book = Book()
        book.delete(id)
    
    @staticmethod
    def search(name_find: str):
        book = Book()
        list_book = book.search(name_find)
        return list_book
    
    @staticmethod
    def search_IU():
        menu_search('Libro', BookController)