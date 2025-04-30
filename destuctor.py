class fruit:

    def __del__(self):
         print('destructor called, fruit deleted.')

obj = fruit()
del obj         