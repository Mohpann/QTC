# Sometimes you want something to execute only if certain conditions are true

# In this case, we want to execute a certain block of code only if the average trade size is greater than or equal to 500 
# and the total weekly trade count is greater than or equal to 2.

tradeSize = 550; 
tradeCount = 3;

if (tradeSize >= 500) & (tradeCount >= 2):
    print("We can execute the block of code") # This will print to the console only if tradeSize and tradeCount are both greater than or equal to 500 and 2 respectively
else:
    print("We cannot execute the block of code") # This will print if tradeSize and tradeCount are not BOTH greater than or equal to 500 and 2 respectively