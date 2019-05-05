
stockList = ('AAPL','AMZN','MSFT','GOOG','FB','JPM','JNJ','GOOGL','XOM','BAC','BRK.B','WMT','V','PFE','UNH','WFC','T','HD','CVX','MA','BABA','NVDA','CLDR','GM','LOGI')

print(str(stockList[4]))

f = open("/home/redman775/python_workspace/test2/datafiles/AMZN.csv", "r")
dataset = f.read()
print(dataset)
print("Done")