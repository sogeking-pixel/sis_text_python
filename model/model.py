import os
from abc import ABC, abstractmethod


class Model_File():
    def __init__(self) -> None:
        self.file_name = None
        self.size = None
    
    @abstractmethod 
    def construir_dict(self, datos): 
        pass
    
    def _save_data(self, data:str)->None:
        if not os.path.exists(self.file_name):
            os.makedirs(os.path.dirname(self.file_name), exist_ok=True)
            with open(self.file_name, "w") as f:
                f.write("0\n"+ str(self.size)+"\n")                
        
        with open(self.file_name, "r+") as f:
           
            lines = f.readlines()
            num = int(lines[0].strip())
            
            f.write(data)
            
            num += 1
            lines[0] = f"{num}\n"
            
            f.seek(0)
            f.writelines(lines)
    
    def get_all(self)->list:  
        if not os.path.exists(self.file_name):
           return []          
        
        with open(self.file_name, "r+") as f:
           
            lines = f.readlines()
            num = int(lines[0].strip())
            size = int(lines[1].strip())
            
            list_data = []
            
            for i in range(num):
                
                data = lines[i*size + 2 : i*size + 2 + size]
                
                dict_data = self.construir_dict(data)
                
                list_data.append( dict_data )   
            
        return list_data
      
    def get_index(self,index: int)->dict:
        if not os.path.exists(self.file_name):
           return {}        
        
        with open(self.file_name, "r+") as f:
           
            lines = f.readlines()
            num = int(lines[0].strip())
            size = int(lines[1].strip())
            
            if num <= index:
                return {}
            
            data = lines[index*size + 2 : index*size + 2 + size]
            
            return self.construir_dict(data)  
       
    def delete(self, id: str)->None:
        if not os.path.exists(self.file_name):
            return        
        
        with open(self.file_name, "r+") as f:                      
            lines = f.readlines()
            
        num = int(lines[0].strip())
        size = int(lines[1].strip())
        
        copy = lines[2:]
        
        i = copy.index(id+'\n')
        
        if i % size != 0 or i == -1:
            return
        
        start = i 
        end = i + size 
        del copy[start:end]
        num -= 1
        
        new_line = [f"{num}\n", f"{size}\n"] + copy
            
        with open(self.file_name, "w") as f:
            f.writelines(new_line)
            
    def get_id(self,id: str)->dict:
        if not os.path.exists(self.file_name):
            return {}        
        
        with open(self.file_name, "r+") as f:
            
            lines = f.readlines()
            num = int(lines[0].strip())
            size = int(lines[1].strip())
            
            for i in range(num):
                if lines[i*size + 2].strip() == id:
                    data = lines[i*size + 2 : i*size + 2 + size]
                    return self.construir_dict(data)
            return {}
    
    def search(self, name:str)->list:
        if not os.path.exists(self.file_name):
            return          
        
        with open(self.file_name, "r+") as f:
            
            lines = f.readlines()
            num = int(lines[0].strip())
            size = int(lines[1].strip())
            
            list_data = []
            
            for i in range(num):
                
                name_autor = lines[i*size+3].strip()
                
                if name_autor.find(name) == -1:
                    continue
                
                data = lines[i*size + 2: i*size + 2 + size]
                
                list_data.append( self.construir_dict(data))
            
        return list_data