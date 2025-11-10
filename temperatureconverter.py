"""
File: temperatureconverter.py
Description: A GUI-based temperature converter between Fahrenheit and Celsius
             using breezypythongui. The window contains two labeled text fields
             and two buttons to convert in both directions.
"""

from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    
   
    def __init__(self):
        
                
        EasyFrame.__init__(self, title="Temperature Converter")

        # Labels
        
        self.addLabel(text="Fahrenheit", row=0, column=0)
        self.addLabel(text="Celsius", row=0, column=1)

        # Text fields with default values
        
        self.fahrField = self.addFloatField(value=32.0, row=1, column=0, precision=2)
        self.celsiusField = self.addFloatField(value=0.0, row=1, column=1, precision=2)

        # Buttons
        
        self.addButton(text=">>>>", row=2, column=0, command=self.convertToCelsius)
        self.addButton(text="<<<<", row=2, column=1, command=self.convertToFahrenheit)

    # Convert Fahrenheit to Celsius
    
    def convertToCelsius(self):
        
                
        fahrenheit = self.fahrField.getNumber()
        celsius = (fahrenheit - 32) * 5 / 9
        self.celsiusField.setNumber(celsius)

    # Convert Celsius to Fahrenheit
    
    def convertToFahrenheit(self):
    
        celsius = self.celsiusField.getNumber()
        fahrenheit = (celsius * 9 / 5) + 32
        self.fahrField.setNumber(fahrenheit)


# Main function
def main():
        TemperatureConverter().mainloop()


if __name__ == "__main__":
    main()
