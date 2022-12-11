class roiCalculator():
    """
        Prompts user to inter information until all fields are entered and then 
        returns a percentage.
    """
    def __init__(self):
        print("Rental Property Assessment-inator.")
        self.name = input("What would you like to name this property? ")
        self.roi = 0
        self.income = {}
        self.total_income = 0
        self.expenses = {'Taxes': 0, 'Insurance': 0, 'Utilities': 0, 'HOA': 0, 'Lawn': 0, 
                         'Vacancy': 0, 'Repairs': 0, 'Capital Expenses': 0, 
                         'Property Management': 0, 'Mortgage': 0}
        self.total_expenses = 0
        self.investments = {'Downpayment': 0, 'Closing Costs': 0, 'Rehab budget': 0}
        self.total_invest = 1 # to protect from dividing by 0 in self.finalSummary, modified to 0 in self.investmentCalculator
        
        self.incomeCalculator()


    def incomeCalculator(self):
        """
            Prompts user to enter rental income as well as asking for any other 
            income the property might bring
        """
        print("\n*** INCOME ***")
        while True:
            response = input(f"What is the source of this income on the {self.name} property? ")
            
            try:
                self.income[response] = float(input("How much income are you expecting this source to bring in PER MONTH? "))
            except:
                print("Please enter a number.")

            response = input("Is there another source of income for this property? (y/n) ")
            if response.lower() == 'y':
                continue
            else:
                for k,v in self.income.items():
                    print(f"{k}: {v}")
                    self.total_income += v
                print(f"Total income: {self.total_income}")
                break
        self.expensesCalculator()

    def expensesCalculator(self):
        print("\n*** EXPENSES ***")

        for k,v in self.expenses.items():
            if k == 'Vacancy':
                question = input(f"How much are you setting aside for {k.lower()} PER MONTH? (Defaults to %5) ")
                try:
                    self.expenses[k] = float(question)
                except:
                    self.expenses[k] = float(self.total_income * 0.05)

            elif k == 'Property Management':
                question = input(f"How much are you setting aside for {k.lower()} PER MONTH? (Defaults to %10) ")
                try:
                    self.expenses[k] = float(question)
                except:
                    self.expenses[k] = float(self.total_income * 0.1)

            elif k == 'Repairs':
                question = input(f"How much are you setting aside for {k.lower()} PER MONTH? (Defaults to $50) ")
                try:
                    self.expenses[k] = float(question)
                except:
                    self.expenses[k] = 50.00

            elif k == 'Capital Expenses':
                question = input(f"How much are you setting aside for {k.lower()} PER MONTH? (Defaults to $100) ")
                try:
                    self.expenses[k] = float(question)
                except:
                    self.expenses[k] = 100.00

            else:
                try:
                    self.expenses[k] = float(input(f"How much are you expecting the {k.lower()} to cost PER MONTH? "))
                except:
                    print("Please enter a number.")

        while True:
            more_expenses = input("Are there any other expenses? (y/n) ")
            
            if more_expenses.lower() == 'y':
                expense = input(f"What expense would you like to add to the {self.name} rental analysis? ")
                try:
                    amount = float(input(f"How much would {expense} cost? "))
                    self.expenses[expense] = amount
                    self.total_expenses += amount
                except:
                    print("Please enter a number")
            else:
                print("*** EXPENSES ***")
                for k,v in self.expenses.items():
                    print(f"{k}: {v}")
                    self.total_expenses += v
                print(f"Total expenses: {self.total_expenses}")
                break

        print(f"Expected Cash Flow: {self.total_income - self.total_expenses}")
        self.investmentCalculator()

    def investmentCalculator(self):
        self.total_invest = 0
        print("*** TOTAL INVESTMENT ***")

        for k,v in self.investments.items():
            try:
                amount = float(input(f"{k}: "))
                self.investments[k] += amount
                self.total_invest += amount
            except:
                print("Please enter a number.")
        while True:
            question = input("Would you like to include any other investments?(y/n) ")
            if question.lower() == 'y':
                add_invest = input("What is the name of the investment? ")
                try:
                    amount = float(input(f"How much will {add_invest} cost? "))
                    self.investments[add_invest] = amount
                    self.total_invest += amount
                except:
                    print("Please enter a number")
            else:
                break
        try:
            self.roi = ((self.total_income * 12) / self.total_invest) * 100
        except:
            print("That's a stupid good deal! Take it!")
        self.finalSummary()

    def finalSummary(self):
        print("*** SUMMARY ***")
        print(f"Assessment of the {self.name} rental property:")
        print("INCOME")
        for k,v in self.income.items():
            print(f"{k}: {v}")
        print(f"Total Income: {self.total_income}")
        print("EXPENSES")
        for k,v in self.expenses.items():
            print(f"{k}: {v}")
        print(f"Total Expenses: {self.total_expenses}")
        print(f"CASH FLOW: {self.total_income - self.total_expenses}")
        print(f"Total Investment: {self.total_invest}")
        print(f"Cash on Cash ROI: %{self.roi}")


test = roiCalculator()
