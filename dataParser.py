#Çağdaş Cemre Yurtsuz

import pandas as pd

class dataParser:

    '''
    This class uses pandas module to I/O operations on excel.
    '''
    def __init__(self, file):

       '''
       Constructer takes a file path and initializes it. 
       '''
       self.file = file




    def parse(self, file):
        '''
        This method takes all the data, put it in a pandas dataframe
        and organizes the dataframe into a python dictionary (I don't trust dataframes).
        '''
        all_rec = dict()
        self.df = pd.read_csv(self.file)

        


        #print(len(df.index))
        
        for col in self.df.columns:
            all_rec[col] = list()


        for i in range(len(self.df.index)):

            for col in all_rec.keys():
                all_rec[col].append(self.df[col][i])
                


        return  all_rec, len(self.df.index)


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

        
        

        
