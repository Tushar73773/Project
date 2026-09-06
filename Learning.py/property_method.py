class tushar:
    @property
    def name(self):
        return f"first name is {self.fname} and last name is {self.lname}"
        

    @name.setter
    def name(self,value):
        self.fname=value.split()[0]
        self.lname=value.split()[1]


a=tushar()
a.name="tushar tiwari"
print(a.name)
