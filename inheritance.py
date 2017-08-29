class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("last name: "+self.last_name)
        print("eye_color: "+self.eye_color)
    
class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = toys
    

billy_cyrus = Parent('Cyrus', 'blue')

billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", 'blue', 5)
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)

miley_cyrus.show_info()
