import os
from .model import Model_File

class User(Model_File):
    def __init__(self) -> None:
        self.file_name = 'archivosxd/txt/user.txt'
        self.size = 3
    
    def construir_dict(self, datos: list)->dict: 
       return {
            'id':datos[0].strip(),
            'name':datos[1].strip(),
            'age': int(datos[2])
        }
    
    def save(self, id: str, name: str, age: int) -> None:
        data = f"{id}\n{name}\n{age}\n"
        self._save_data(data)

    def update(self, id: str, name = None, age = None )->None:
        
        if name is None and age is None:           
            return
        
        if type(age) != int and age is not None:
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
                                
                    if name is not None:                       
                        lines[i*size + 3] = name + '\n'
                    if age is not None:
                        lines[i*size+4] = str(age) + '\n'
                    
                    break
            
            if b == -1:
                return           
            
            f.seek(0)
            f.writelines(lines)        
            
        return
               