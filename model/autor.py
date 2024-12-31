import os
from .model import Model_File

class Autor(Model_File):
    def __init__(self) -> None:
        self.file_name = 'archivosxd/txt/autor.txt'
        self.size = 3
    
    def construir_dict(self, datos: list)->dict: 
       return {
            'id':datos[0].strip(),
            'name':datos[1].strip(),
            'nacionality': datos[2].strip()
        }
    
    
    def save(self, id: str, name: str, nacionality:str) -> None:
        data = f"{id}\n{name}\n{nacionality}\n"
        self._save_data(data)
       

    def update(self, id: str, name = None, nacionality = None )->None:
        if name is None and nacionality is None:           
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
                    if nacionality is not None:
                        lines[i*size+4] = nacionality + '\n'
                    
                    break
            
            if b == -1:
                return           
            
            f.seek(0)
            f.writelines(lines)        
            
        return
    
    