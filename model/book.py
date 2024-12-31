import os
from .model import Model_File

class Book(Model_File):
    def __init__(self) -> None:
        self.file_name = 'archivosxd/txt/book.txt'
        self.size = 6
    
    def construir_dict(self, datos: list)->dict: 
       return {
            'id':datos[0].strip(),
            'title':datos[1].strip(),
            'num_page': int(datos[2]),
            'date_created': datos[3].strip(),
            'id_autor': datos[4].strip(),
            'status': bool(datos[5])             
        }
    
    
    def save(self, id: str, title: str, cant_page: int, date_created: str, id_autor: str) -> None:
        data = f"{id}\n{title}\n{cant_page}\n{date_created}\n{id_autor}\n{True}\n"
        self._save_data(data)
       

    def update(self, id: str, title = None, cant_page = None, date_created = None, id_autor = None , status = None)->None:
        if title is None and cant_page is None and date_created is None and id_autor is None and status is None:           
            return
        
        if type(cant_page) != int and cant_page is not None:
            return
        
        if type(status) != bool and status is not None:
            return
        
        if not os.path.exists(self.file_name):
           return      
        
        with open(self.file_name, "r+") as f:
            lines = f.readlines()
            num = int(lines[0].strip())
            size = int(lines[1].strip())
            b = -1
            for i in range(num):
                if lines[i*size + 2].strip() == id:
                    b=i  
                                                    
                    if title is not None:                       
                        lines[i*size + 3] = title + '\n'
                    if cant_page is not None:
                        lines[i*size+4] = str(cant_page) + '\n'
                    if date_created is not None:
                        lines[i*size+5] = date_created + '\n'
                    if id_autor is not None:
                        lines[i*size+6] = id_autor + '\n'
                    if status is not None:
                        lines[i*size+7] = str(status) + '\n'
                    break
            
            if b == -1:
                return           
            
            f.seek(0)
            f.writelines(lines)        
            
        return
    