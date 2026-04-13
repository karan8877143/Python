# Create a Temperature class. Create 2 methods named convertFarenheit() and convertCelsius().

class Temperature:
    def convertFarenheit(self):
        self.cel=int(input("enter temperature in cel: "))
        f=(self.cel * 9/5)+32
        print("Farenheit: ",f)
     
    def convertCelcius(self):
        self.f=int(input("enter temperature in feh: "))
        cel= (self.f - 32) * 5/9
        print("Celcius: ",cel)
obj=Temperature()
obj.convertFarenheit()
obj.convertCelcius()