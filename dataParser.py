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
    def write(self, weekly_plan, startDate):
        # Create a Pandas dataframe from the data.

        
        
        s = list()

        
        i = 1
        for week in weekly_plan:

            for job in week:
                self.df.loc[self.indMap[job], 'updRolloutDate'] = f'{startDate[0]}-{i}'

            if i % 52 == 0:
                startDate[0] += 1
                i = 0

            i += 1
           
        writer = pd.ExcelWriter('RecommendationPlan.xlsx', engine='openpyxl') 
        wb  = writer.book

        self.df.to_excel(writer, index=True)
        wb.save('RecommendationPlan.xlsx')
        '''
        

