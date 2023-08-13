#!/usr/bin/env python
# coding: utf-8

# In[25]:


#INTRO
print("Hong Kong stock trading calculator 1.0")
print("======================================================")
print("This app calculates the net profit when trading with Hong Kong stocks. While the fees are based on Fidelity rates, it can be used for any broker. Just update the variables with the rates of your desired broker.")
fidcom = 250
print("Commission fee: "+ str(fidcom)+' HKD')
fidset = 0.0014
print("Settlement fee: "+ str(fidset)+'%')
HKD = 7.82
print("Current exchange rate: "+ "1 USD = " + str(HKD)+' HKD')
print("======================================================")

class SellAmountError(Exception):
    "Raised when selling amount exceeds buying amount."
    pass

def netprofit(ibuy, isell):
    buy = ibuy + fidcom + fidset*ibuy
    sell = isell - fidcom - fidset*isell
    profit = sell - buy
    return profit

while True:
    
    try:
        #get input from prompt for buy
        buyamount = float(input("Enter buying amount of shares: "))
        print("Buying amount of shares: " + str(buyamount))
        buyprice = float(input("Enter buying price in HKD: "))
        print("Buying price in HKD: " + str(buyprice))
        buytotal = buyamount*buyprice
        print("Buying total in HKD: " + str(buytotal))
        
        #get input from prompt for sell & check if selling amount does not exceed buying amount and is greater than 0
        sellamount = float(input("Enter selling amount of shares: "))
        print("Selling amount of shares: " + str(sellamount))
        
        if (sellamount > buyamount) or (sellamount <= 0):
            raise SellAmountError
        else:
            sellprice = float(input("Enter selling price in HKD: "))
            print("Selling price in HKD: " + str(sellprice))
            selltotal = sellamount*sellprice
            print("Sell total in HKD: " + str(selltotal))
        break
        
    except ValueError:
        print("Enter only numbers, please!")
        
    except SellAmountError:
        print("Invalid entry! Selling amount must be greater than 0 and must not exceed buying amount!")

#perform calculation
print("======================================================")
print("Transaction costs in HKD: " + str((round(2*fidcom+fidset*(buytotal+selltotal),2))))
print("Transaction costs in USD: " + str((round((2*fidcom+fidset*(buytotal+selltotal))/HKD,2))))
percent = (selltotal-fidcom-fidset)/(buytotal+fidcom+fidset)
print("Net profit in %: " + str(round((percent-1)*100,2)))
print("Net profit in HKD: " + str(round(netprofit(buytotal, selltotal),2)))
print("Net profit in USD: " + str(round(netprofit(buytotal, selltotal)/HKD, 2)))

