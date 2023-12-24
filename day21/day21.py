# Exercise Level 1

# Python has the module called _statistics_ and we can use this module to do all the statistical calculations.
import math

class statistics:
    def __init__(self, items=[]):
        self.items = items

        def mean(self):
            try:
              return sum(self.items) / len(self.items)
            except:
                return "List is empty"
            
            def median(self):
                if len(self.items)%2 == 0:
                    return self.items[len(self.items)//2:len(self.items)//2+2]
                else:
                    return self.items[len(self.items)//2]
                
            def mode(self):
                hash = {}
                for i in self.items:
                    if hash.get(i):
                        hash[i]+=1
                    else:
                        hash[i]=1
                        sorted_hash = sorted(hash.items(),key=lambda x: x[1],reverse=True)
                        return sorted_hash[0][0]
                    
                    def range(self):
                        return max(self.items) - min(self.items)
                
# To calculate the variance take each difference square it and then average the result:
def variance (self):
    arr_sum = 0
    for i in self.items:
        arr_sum+=(i - self.mean()) ** 2

        return round(arr_sum/len(self.items),2)
    
def standard_deviation(self): 
    return round(math.sqrt(self.variance()))

def min(self):
    return min(self.items)

def math(self):
    return max(self.items)

def count(self,element):
    hash = {}
    for i in self.items:
        if hash.get(i):
            hash[i]+=1
        else:
            hash[i]=1
            return hash[element]
    
# percentile, and frequency distribution
ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]
data = Statistics(ages)

print(data.mean())
print(data.median())
print(data.mode())
print(data.range())
print(data.count())
print(data.variance())
print(data.standard_deviation())

# Create a class called PersonAccount.
# It has
# firstname,
# lastname,
# incomes,
# expenses properties,
# and it has total income,
# total_expense,
# account_info,
# add_income,
# add_expense
# and account_balance methods.
# incomes is a set of incomes and its description. The same goes for expenses.