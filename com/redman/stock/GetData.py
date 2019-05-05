import requests




url = 'https://marketdata.websol.barchart.com/getHistory.csv?apikey=<myKey>&symbol=AMZN&type=daily&startDate=20180401000000'
response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print('First 100 characters of data are')
    print(response.text[:100])
    f = open("/home/redman775/python_workspace/test2/datafiles/test.csv", "w")
    f.write(response.text)
    f.close()

print("Done")
