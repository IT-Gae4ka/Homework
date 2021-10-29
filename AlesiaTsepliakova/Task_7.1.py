# Task 7.1
# Implement class-based context manager for opening and working with file, including handling exceptions. Do not use 'with open()'. Pass filename and mode via constructor.
  
class FileManager():
    modes = ['r', 'w', 'a', 'r+']
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

          
    def __enter__(self):
        try:
            self.mode in self.modes
            self.file = open(self.filename, self.mode)
            return self.file
        except ValueError:
            print("Please write the name of the file or the right mode in your input!")            
        except FileNotFoundError as not_found_e:
            print(f"Please write the name of the file in your input!\n Your error is: {not_found_e}")
    
        
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is not None:
            print(f"Excepion type: {exc_type},\nExcepion value: {exc_value}, \nException traceback: {exc_traceback}")
        self.file.close()
      

with FileManager('text.txt', 'w') as f:
    f.write('Test')
  
with FileManager('text.txt', 'r') as f:
    print(f.read())
