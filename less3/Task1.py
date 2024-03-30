class C:
    def __init__(self, name):
        self.name = name
        pass
    def get_name(self):
        print(f"Method name: {self.name}")
        pass
my_c = C('Abstract')
my_c.get_name()
print(f'')