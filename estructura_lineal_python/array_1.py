class Array:
    def __init__(self, dimension, valor = None):
        self.items = []
        for i in range(dimension):
            self.items.append(valor)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __get__(self, index):
        return self.items[index]
    
    def __upgrade__(self, index, new_item):
        self.items[index] = new_item
