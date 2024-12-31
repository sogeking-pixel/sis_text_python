from model.book import Book
from model.user import User
from model.prestamo import Loands
from view.crud import menu_crud_prestamo
from view.create import menu_create
from view.delete import menu_delete
from view.loand_return import menu_loan



class LoanController():
    @staticmethod
    def index()->None:
        menu_crud_prestamo( LoanController)
    
    @staticmethod    
    def show(id: str)->dict:
        loan = Loands() 
        data_loan = loan.get_id(id)
        return data_loan
    
    @staticmethod
    def edit():
        menu_loan( LoanController)
    
    @staticmethod
    def store(id: str, id_user: str, id_book: str, day_increment: str):
        user = User()
        book = Book()
        
        if user.get_id(id_user) is None:
            return False
        
        book_data = book.get_id(id_book)
        
        if book_data is None:
            return False
        
        if not book_data['status']:
            return
        
        del book_data
        
        loan = Loands()
        
        from datetime import datetime, timedelta
        
        now = datetime.now()        
        date_will = now + timedelta(days= int(day_increment))

        date_will_str = date_will.strftime("%Y/%m/%d %H:%M:%S")
        date_now_str = now.strftime("%Y/%m/%d %H:%M:%S")
        loan.save(id,id_user,id_book, date_now_str, date_will_str)
        book.update(id_book,status=False)
    
    @staticmethod
    def create():
        list_parameters = ['id','id_user', 'id_book','day_increment']
        menu_create('Prestamo', LoanController, list_parameters)
    
    @staticmethod
    def return_loan(id: str)->bool:
        loan = Loands()       
        data_loan = loan.get_id(id)        
        if data_loan is None:
            return False
        
        book = Book()
        book.update(data_loan['id_book'],status=True)
        
        from datetime import datetime
        
        date_return = datetime.now()        

        date_return_str = date_return.strftime("%Y/%m/%d %H:%M:%S")

        b =  data_loan['date_deadline'] < date_return_str
              
        loan.update(id = id,date_return=date_return_str, sanctions=b)
        
        return True
    
    @staticmethod
    def delete():
        menu_delete('Prestamo', LoanController)
    
    @staticmethod
    def destroy(id: str):
        loan = Loands()
        loan.delete(id)
    