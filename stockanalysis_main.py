import sys

with open("bankniftyeq.csv") as fl:
    flwrt = open("bankniftyeq_modified.csv",'w')
    count = 0
    for line in fl.readlines():
#         print line
        elements = line.split(',')
        for i in range(0,len(elements)-1,8):
            flwrt.write(",".join(elements[i:i+8])+'\n')
        count +=1
#         if count ==5:
#             break
dict_index = {"BANKNIFTY":1,
              "AXISBANK":3.991028,
              "BANKBARODA":2.255481,
              "BANKINDIA":0.557501,
              "CANBK":0.440772,
              "FEDERALBNK":4.10791,
              "HDFCBANK":4.787828,
              "ICICIBANK":13.88942,
        "INDUSINDBK":1.181981,
        "KOTAKBANK":2.761566,
        "PNB":    1.781471,
        "SBIN":    7.413441,
        "YESBANK":    0.784409,
                }
def build_map():
    dic_time_instruments = {}
    with open("bankniftyeq_modified.csv") as fl:
        count = 0
        for line in set(fl.readlines()):
    #         print line
            elements = line.split(',')
            if len(elements) == 8:
                time_stamp_with_second = elements[0]
                time_stamp = time_stamp_with_second.split('.')[0]
                if dic_time_instruments.has_key(time_stamp):
                    dic_time_instruments[time_stamp].append(tuple(elements[1:])) 
                else:
                    dic_time_instruments[time_stamp] = [tuple(elements[1:])]
            else:
                continue
                
    print len(dic_time_instruments)
#     print dic_time_instruments['09:20:00']   
    return dic_time_instruments 

def get_unique_instruments(value):
    dic_temp = {}
    for items in value:
        if dic_temp.has_key(items[0]):
            dic_temp[items[0]] += int(items[6].strip('\n'))
        else:
            dic_temp[items[0]] = int(items[6].strip('\n'))
            
    return dic_temp.items()    
    
if __name__ == '__main__':
    print dict_index['BANKBARODA']
    dic_time_instruments = build_map()
    index_value = 0
    fl = open("time_index_value.txt",'w')
    for key,value in dic_time_instruments.iteritems():
        instrument_names =''
        print "key"+key
        print "value##",value
        value = get_unique_instruments(value)
        print "value##2",value
#         sys.exit()
        for items in value:
            index_value += dict_index[items[0][:-3]]*float(items[len(items)-1])
            instrument_names +=items[0] +" "
#         print key,index_value/len(value) ,index_value, instrument_names
        fl.write((key+' '+str(index_value/len(value))+' '+instrument_names).strip()+'\n')
    fl.close()