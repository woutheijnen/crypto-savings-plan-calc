import datetime
filepath = 'gemini_BTCUSD_1hr.csv'
# DL: http://www.cryptodatadownload.com/data/binance/
# Take data for last 4 years only starting at end of last month
# And don't forgot to add 29th, 30th day to februaries'
results = {}
used = {}
with open(filepath) as fp:
    line = fp.readline()
    while line:
        data = line.strip().split(",")
        # For binance : dtime = datetime.datetime.fromtimestamp(int(data[0].replace(".0", "000"))/1000)
        # For weekly :        
        #dtimeStr = dtime.strftime("%A %H:%M:%S")
        # For monthly :        
        # For binance : dtimeStr = dtime.strftime("%d %H:%M:%S")
        dtimeStr= data[1][-11:]
        if dtimeStr not in results:
            results[dtimeStr] = 0.0
            used[dtimeStr] = 0
        results[dtimeStr] += 50 / float(data[3])
        used[dtimeStr] += 50
        line = fp.readline()

highest = ""
for result in results:
    results[result] = results[result] / (used[result] / 50)
    if highest == "":
        highest = result
    if results[result] > results[highest]:
        highest = result

print(results)
print(highest)
print(results[highest])
