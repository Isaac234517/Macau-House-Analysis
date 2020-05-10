import pandas as pd
import numpy as np

def get_dsf_building_df(file_name, year, month):
    result = pd.read_excel(file_name, sheet_name="Sheet0",  skiprows=1)
    result = result.rename(columns= {"區域": "Area", "大廈名稱":"Building_Name", "成交量":"Volume", "平均樓價($/㎡)": "Price/㎡"})
    result = result[np.isnan(result['Volume']) == False]
    month_arr = [month] * result.shape[0]
    year_arr =[year] * result.shape[0]
    result['Year'] = year_arr
    result['Month'] = month_arr
    result = result[['Year', 'Month', 'Area', 'Building_Name', 'Volume', 'Price/㎡']]
    return result
