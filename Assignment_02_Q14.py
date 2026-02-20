class BookAlloment:
    def __init__(self,standard,notebooks,pages):
        self.standard = standard
        self.notebooks  = notebooks
        self.pages = pages


        self.book_price ={"Hindi":[60,100,150],
                          "Marathi":[60,100,150],
                          "English":[80,100,150],
                          "Science":[90,120,200],
                          "Maths": [100,140,250],}
        self.notebooks_prices = {
            "square": [40,70],
            "4lines":[30,50],
            "2lines":[30,50],
            "single lines": [60,100],
            "A4 notebook": [100,180],
        }
        
    def get_standard_index(self):
        if self.standard in ["1st","2nd","3rd","4th"]:
            return 0
        elif self.standard in ["5th","6th","7th","8th"]:
            return 1
        elif self.standard in ["9th","10th"]:
             return 2
        else:
            return -1
        
    def calculate_books_cost(self):
        index = self.get_standard_index()
        if index == -1:
            return 0
        
        total = 0
        for price in self.book_price.values():
            total += price[index]
        return total
    
    def calculate_notebook_cost(self):
        page_index = 0 if self.pages == 100 else 1

        total = 0
        for nb in self.notebooks:
            total += self.notebooks_prices[nb][page_index]
        return total
    
    def total_cost(self):
        return self.calculate_books_cost() + self.calculate_notebook_cost()
    

standard = input("Enter standard (1st–10th): ")

n = int(input("How many notebook types do you want? "))
notebooks = []
for _ in range(n):
    nb = input("Enter notebook type (square/4lines/2lines/single lines/A4 notebook): ")
    notebooks.append(nb)

pages = int(input("Enter pages (100 or 200): "))

student = BookAlloment(standard, notebooks, pages)

print("Total Books Cost:", student.calculate_books_cost())
print("Total Notebook Cost:", student.calculate_notebook_cost())
print("Total Amount to Pay:", student.total_cost())
                
