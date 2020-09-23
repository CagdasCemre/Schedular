#Çağdaş Cemre Yurtsuz

import pandas as pd
from SNP_Lib.PE import network_element
from math import isnan

class dataParser:


    def __init__(self):
        pass
     

    def dateParser(date):
        #Split the date components into yy-ww
        spltDate = date.split('-')
       

        date = list()
        

        
        for i in spltDate:
            date.append(int(i))
            

        return date




    
    def parse(self, file):
      
        
        self.df = pd.read_csv(file, low_memory=False)
        self.all_rec = list()

        

        #print(len(self.df.index))

        self.indMap = list()
        nCount = 0
        for i in range(len(self.df.index)):

            

                
              newObj = network_element()
              newObj.region = self.df['region'][i]
              newObj.site = self.df['site'][i]
              newObj.status = self.df['status'][i]      

              if self.df['dayVol'][i] is not None:
                 newObj.dayVol = self.df['dayVol'][i]
                        
              newObj.priority = self.df['priority'][i]
              newObj.groupID = self.df['groupID'][i]            
              nCount += 1
                
              
              self.all_rec.append(newObj)

            
        return  self.all_rec, nCount
        
   '''
    def write(recomList):
        # Create a Pandas dataframe from the data.

        
        date_list = list()

        for recom in recomList:
            if recom.status == 'Optional' and recom.updRolloutDate is not None :
                date_list.append(recom.updRolloutDate)

        num_list = list()
        for date in date_list:
            num_list.append(int(date[date.find('-')+1:]))

        weekLim = max()
            
        df = pd.DataFrame(num_list)
           
        writer = pd.ExcelWriter('RecommendationPlan.xlsx', engine='openpyxl') 
        wb  = writer.book

        df.to_excel(writer, index=True)
        wb.save('RecommendationPlan.xlsx')
   '''
        

