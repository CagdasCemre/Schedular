import pickle
import datetime
import copy
from schedular import schedular
from dataParser import dataParser

endDateTime = datetime.datetime.strptime("01.01.2023", "%d.%m.%Y").date()
startDateTime = datetime.datetime.strptime("01.01.2021", "%d.%m.%Y").date()
noOfDays = (endDateTime - startDateTime).days
        # ************************************************************************
        # DETERMINE FORECASTING INTERVAL
processInterval = []
indexList = []
counter = 0
for x in range(0, noOfDays):
    counter = counter + 1
    indexList.append(counter)
    processInterval.append((startDateTime + datetime.timedelta(days=x)))
        # ************************************************************************
        
        # WEEK AGGREGATION
newProcessInterval = []
for each in processInterval:
    dummy = each.strftime('%Y') + '-' + each.strftime('%W')
    newProcessInterval.append(dummy)
processInterval = copy.deepcopy(set(newProcessInterval))
processInterval = sorted(processInterval)



dataparser = dataParser()

recomLst, nCount = dataparser.parse('C:/Users/cemre.yurtsuz/Desktop/Schedular/P2_SNP_Recommendations_2020_09_15_11_47_22/P2_SNP_Recommendations_2020_09_15_11_47_22.csv')

recomLst = schedular(recomLst, ['2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06', '2021-07', '2021-08', '2021-09', '2021-10', '2021-11', '2021-12', '2021-13', '2021-14', '2021-15', '2021-16', '2021-17', '2021-18', '2021-19', '2021-20', '2021-21', '2021-22', '2021-23', '2021-24', '2021-25', '2021-26', '2021-27', '2021-28', '2021-29', '2021-30', '2021-31', '2021-32', '2021-33', '2021-34', '2021-35', '2021-36', '2021-37', '2021-38', '2021-39', '2021-40', '2021-41', '2021-42', '2021-43', '2021-44', '2021-45', '2021-46', '2021-47', '2021-48', '2021-49', '2021-50', '2021-51', '2021-52', '2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06', '2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12', '2022-13', '2022-14', '2022-15', '2022-16', '2022-17', '2022-18', '2022-19', '2022-20', '2022-21', '2022-22', '2022-23', '2022-24', '2022-25', '2022-26', '2022-27', '2022-28', '2022-29', '2022-30', '2022-31', '2022-32', '2022-33', '2022-34', '2022-35', '2022-36', '2022-37', '2022-38', '2022-39', '2022-40', '2022-41', '2022-42', '2022-43', '2022-44', '2022-45', '2022-46', '2022-47', '2022-48', '2022-49', '2022-50', '2022-51', '2022-52'])

