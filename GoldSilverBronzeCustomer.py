#Are you a Gold, Silver, or Bronze customer?

annualSales = 200000
newCustomer = True

if annualSales >= 500000:
    print("Gold Customer")
elif annualSales >= 300000:
    print("Silver Customer")
elif annualSales >= 100000 and newCustomer == True:
    print ("Bronze Customer and First-time Prize Winner")
elif annualSales >= 100000:
    print("Bronze Customer")
    
print("Thank you for your business")
