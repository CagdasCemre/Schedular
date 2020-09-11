#Çağdaş Cemre Yurtsuz

import pandas as pd
from NE_Obj import network_element


class dataParser:

    '''
    This class uses pandas module to I/O operations on excel.
    '''
    def __init__(self, file):

       '''
       Constructer takes a file path and initializes it. 
       '''
       self.file = file




    def parse(self):
        '''
        This method takes all the data, put it in a pandas dataframe
        and organizes the dataframe into a python dictionary (I don't trust dataframes).
        '''
        
        df = pd.read_csv(self.file, low_memory=False)
        all_rec = [network_element() for _ in range (len(df.index))]
        


        #print(len(df.index))


        for i in range(len(df.index)):

            all_rec[i].region = df['region'][i]
            all_rec[i].site = df['site'][i]
            all_rec[i].dayVol = df['dayVol'][i]
            all_rec[i].priority = df['priority'][i]
            all_rec[i].groupID = df['groupID'][i]            
            all_rec[i].status = df['status'][i]
            
        return  all_rec, len(df.index)


    def write(self, weekly_plan, clusterIndex, weekIndex, nCount):
        # Create a Pandas dataframe from the data.

        '''
        This method creates an excel file named RecommendationPlan.xlsx
        and inserts the organised weekly plan into it.
        '''
        
        s = list()

        
        for i in range(nCount):
            s.append(weekIndex[clusterIndex[i]] + 1 )
           
        writer = pd.ExcelWriter('Recommendation.xlsx', engine='openpyxl') 
        wb  = writer.book
        df = pd.DataFrame({'Weeks': s})

        df.to_excel(writer, index=True)
        wb.save('RecommendationPlan.xlsx')

        
        

        
