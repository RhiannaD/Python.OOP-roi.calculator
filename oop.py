# ROI calculator


# 4 methods?

class Roi():
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.cashflow = 0
        self.cash_on = 0
        self.total_expenses =0


    def rental(self):
        house_amt  = int(input("How much is the house?"))
        print(f'your house cost{house_amt}')
        house_div =house_amt / 100
        self.income+=house_div
        extra = input("Anything extra?")
        if extra == 'yes':
            extra_amt =int(input("how much is it?"))
            self.income+= extra_amt
        
        print(f'total monthly rental income{self.income}')
        


    def monthly(self):
        r_expenses = input("do you have any expenses? ")   
        if r_expenses == 'no':
            pass
              
        else:
            amt = int(input("How much is it? "))
            self.expenses[r_expenses]=amt
            self.total_expenses=sum(self.expenses.values())
        

    def total(self):
        self.cashflow = self.income - self.total_expenses
        print(f' Curent cashflow is{self.cashflow}')



    def roi(self):
        house_amt=self.income * 100
        down_pay = int(house_amt*.20)
        invest = input("Any other expenses with closing cost ?")
        if invest == 'yes':
            other_amt = int(input("How much is it?"))
            self.cash_on +=other_amt
            print(self.cash_on)
       
        total_inves =down_pay+self.cash_on
            
    
        annual_cashflow= self.cashflow * 12
        print(f'This is your cash on cash ROI{(annual_cashflow/total_inves)}')

your_roi = Roi()

def runner():
    print("\n-------Welcome to the ROI calculator-------")

    while True:
        start = input("\n\n\nDo you want to know your Monthly Rental Income " +
                    " Monthly Expenses "+" Cash Flow or Cash ROI? ").lower()

        if start == 'monthly rental income':
            your_roi.rental()
        elif start == 'monthly expenses':
            your_roi.monthly()
        elif start == 'cash flow':
            your_roi.total()
        elif start == 'cash roi':
            your_roi.roi()
        elif start == 'quit':
            break
        else:
            return 'Invalid reponse'


print(runner())
        



