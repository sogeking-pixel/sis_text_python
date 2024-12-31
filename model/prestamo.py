import os
from .model import Model_File

class Loands(Model_File):
    def __init__(self) -> None:
        self.file_name = 'archivosxd/txt/loands.txt'
        self.size = 7
    
    def construir_dict(self, datos: list)->dict: 
       return {
            'id':datos[0].strip(),
            'id_user':datos[1].strip(),
            'id_book': datos[2].strip(),
            'date_created': datos[3].strip(),
            'date_deadline': datos[4].strip(), 
            'date_return': datos[5].strip(),             
            'sanctions': bool(datos[6])              
        }
    
    
    def save(self, id: str, id_user: str, id_book: str, date_created: str, date_deadline: str) -> None:
        data = f"{id}\n{id_user}\n{id_book}\n{date_created}\n{date_deadline}\n{None}\n{False}\n"
        self._save_data(data)
       

    def update(self, id: str, id_user = None, id_book = None, date_created = None, date_deadline = None, date_return = None,sanctions = None )->None:
        if id_user is None and id_book is None and date_created is None and date_deadline is None and date_return is None and sanctions is None:           
            return
        
        if type(sanctions) != bool and sanctions is not None:
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
                    
                    if id_user  is not None:
                        lines[i * size + 3] =  id_user + '\n'
                    if id_book  is not None:
                        lines[i * size + 4] = id_book + '\n'
                    if date_created  is not None:
                        lines[i * size + 5] =   date_created + '\n'
                    if date_deadline  is not None:
                        lines[i * size + 6] =  date_deadline + '\n'
                    if date_return is not None:
                        lines[i * size + 7] = date_return + '\n'
                    if sanctions  is not None:
                        lines[i * size + 8] =  str(sanctions) + '\n'
                    
                    break
            
            if b == -1:
                return           
            
            f.seek(0)
            f.writelines(lines)        
            
        return
    
    def search(self):
        pass