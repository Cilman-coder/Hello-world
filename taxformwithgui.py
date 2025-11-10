"""
File: taxformwithgui.py
GUI Tax Calculator
"""
import random
from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Tax Calculator")

        self.addLabel(text="Gross income", row=0, column=0)
        self.incomeField = self.addFloatField(0.0, row=0, column=1)

        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(0, row=1, column=1)

        self.addButton(text="Compute", row=2, column=0, columnspan=2,
                       command=self.computeTax)

        self.addLabel(text="Total tax", row=3, column=0)
        self.taxField = self.addFloatField(0.0, row=3, column=1,
                                           state="readonly")

    def computeTax(self):
        income = self.incomeField.getNumber()
        dependents = self.depField.getNumber()

        # Formula for Tax Calculator
        
        tax = (income * 0.12) - (dependents * 600)
        if tax < 0:
            tax = 0.0

        self.taxField.setNumber(round(tax, 2))


def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()
