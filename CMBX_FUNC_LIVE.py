#==============================================================================
# Load Libraries
#==============================================================================


import pandas as pd
import io
import numpy as np
import mechanize as mh


#==============================================================================
# Change Directory
#==============================================================================


#==============================================================================
# Parse DTCC Website and run analytics on the data
#==============================================================================

# =============================================================================
# browse = mh.Browser()
# browse.open('https://pddata.dtcc.com/gtr/inquiry.do')
# 
# browse.select_form(name='dailySearchForm')
# browse.form['jurisdiction'] = ['CA',]
# browse.form['assetClassification'] = ['CR',]
# browse.form['notionalRange.low'] = '1'
# browse.form['displayType'] = ['c',]
# browse.submit()
# 
# resp = browse.response()
# 
# content = resp.read()
# 
# dtccdata = pd.read_csv(io.BytesIO(content))
# 
# dtccdata.columns
# 
# dtccdata['Notional Amount 1'] = dtccdata['Notional Amount 1'].str.replace(',','')
# if dtccdata['Notional Amount 1'].dtype == 'O':
#     dtccdata['Notional Amount 1'] = np.where(dtccdata['Notional Amount 1'].str.contains('[+]'),dtccdata['Notional Amount 1'].str.replace('+',''),dtccdata['Notional Amount 1'])
#     dtccdata['Notional Amount 1'] = dtccdata['Notional Amount 1'].astype(np.float)
# else:
#     dtccdata['Notional Amount 1'] = dtccdata['Notional Amount 1'].astype(np.float)
#     
# 
# if dtccdata['Price 1'].dtype == 'O':
#     dtccdata['Price 1'] = np.where(dtccdata['Price 1'].str.contains(','),dtccdata['Price 1'].str.replace(',',''),dtccdata['Price 1'])
#     dtccdata['Price 1'] = pd.to_numeric(dtccdata['Price 1'])
# else:
#     dtccdata['Price 1'] = pd.to_numeric(dtccdata['Price 1'])
# 
# 
# dtccdata['CMBX Flag'] = np.where(dtccdata['Underlying Asset Name'].isin(uservariable),1,0)
# 
# 
# filtereddf = dtccdata[dtccdata['CMBX Flag'] == 1]
# filtereddf = filtereddf[filtereddf['Action'] != 'CANCEL']
# 
# =============================================================================
#==============================================================================
# uniquetrades = list(set(filtereddf['UNDERLYING_ASSET_1']))
# 
# def calcs(x):
#     tempsdf = filtereddf[filtereddf['UNDERLYING_ASSET_1']==x]
#     totalnumberofCMBXtrades = sum(tempsdf['CMBX Flag'])
#     avgpriceoftrades = np.mean(tempsdf['PRICE_NOTATION'])
#     averagenotionaloftrades = np.mean(tempsdf['ROUNDED_NOTIONAL_AMOUNT_1'])
#     return [totalnumberofCMBXtrades,avgpriceoftrades,averagenotionaloftrades]
# 
# 
# calcdictionary = {}
# for i in uniquetrades:
#     calcdictionary[i] = calcs(i)
# 
#==============================================================================
 
# =============================================================================
# summarydf = pd.pivot_table(filtereddf,values = ['CMBX Flag','Price 1','Notional Amount 1'],index = ['Underlying Asset Name','Transaction Type'],aggfunc = {'CMBX Flag' : np.sum,'Price 1' : np.mean,'Notional Amount 1':np.mean})
# if len(summarydf)>0:
#     summarydf.columns = ['Count','Average Notional','Average Price']
#     summarydf['Average Notional'] = summarydf['Average Notional'].astype('float')
# 
# =============================================================================

#==============================================================================
# CFTC Form Actions
#==============================================================================

def web_tool_cmbx():
    browse = mh.Browser()
    browse.open('https://pddata.dtcc.com/gtr/inquiry.do')
    
    browse.select_form(name='dailySearchForm')
    browse.form['jurisdiction'] = ['CFTC',]
    browse.form['assetClassification'] = ['CR',]
    browse.form['notionalRange.low'] = '1'
    browse.form['notionalRange.high'] = '5000000000000'
    browse.form['displayType'] = ['c',]
    browse.submit()
    
    resp = browse.response()
    
    content = resp.read()
    
    dtccdata2 = pd.read_csv(io.BytesIO(content))
    
    
    dtccdata2['Notional Amount 1'] = dtccdata2['Notional Amount 1'].str.replace(',','')
    if dtccdata2['Notional Amount 1'].dtype == 'O':
        dtccdata2['Notional Amount 1'] = np.where(dtccdata2['Notional Amount 1'].str.contains('[+]'),dtccdata2['Notional Amount 1'].str.replace('+',''),dtccdata2['Notional Amount 1'])
        dtccdata2['Notional Amount 1'] = dtccdata2['Notional Amount 1'].astype(np.float)
    else:
        dtccdata2['Notional Amount 1'] = dtccdata2['Notional Amount 1'].astype(np.float)
        
    
    if dtccdata2['Price 1'].dtype == 'O':
        dtccdata2['Price 1'] = np.where(dtccdata2['Price 1'].str.contains(','),dtccdata2['Price 1'].str.replace(',',''),dtccdata2['Price 1'])
        dtccdata2['Price 1'] = pd.to_numeric(dtccdata2['Price 1'])
    else:
        dtccdata2['Price 1'] = pd.to_numeric(dtccdata2['Price 1'])
    
    
    uservariable = ['CMBX.NA.BB.6',
    "CMBX.NA.BBB-.6",
    "CMBX.NA.BBB-.11",
    "CMBX.NA.A.6"]
    dtccdata2['CMBX Flag'] = np.where(dtccdata2['Underlying Asset Name'].isin(uservariable),1,0)
    
    
    filtereddf2 = dtccdata2[dtccdata2['CMBX Flag'] == 1]
    filtereddf2 = filtereddf2[filtereddf2['Action'] != 'CANCEL']
    
    #==============================================================================
    # uniquetrades = list(set(filtereddf['UNDERLYING_ASSET_1']))
    # 
    # def calcs(x):
    #     tempsdf = filtereddf[filtereddf['UNDERLYING_ASSET_1']==x]
    #     totalnumberofCMBXtrades = sum(tempsdf['CMBX Flag'])
    #     avgpriceoftrades = np.mean(tempsdf['PRICE_NOTATION'])
    #     averagenotionaloftrades = np.mean(tempsdf['ROUNDED_NOTIONAL_AMOUNT_1'])
    #     return [totalnumberofCMBXtrades,avgpriceoftrades,averagenotionaloftrades]
    # 
    # 
    # calcdictionary = {}
    # for i in uniquetrades:
    #     calcdictionary[i] = calcs(i)
    # 
    #==============================================================================
     
    summarydf2 = pd.pivot_table(filtereddf2,values = ['CMBX Flag','Price 1','Notional Amount 1'],index = ['Underlying Asset Name','Transaction Type'],aggfunc = {'CMBX Flag' : np.sum,'Price 1' : [np.mean,np.max,np.min],'Notional Amount 1':[np.mean,np.sum]})
    if len(summarydf2)>0:
        summarydf2.columns = ['Count','Average Notional','Sum Notional','Max Price','Min Price','Average Price']
        summarydf2['Average Notional'] = summarydf2['Average Notional'].astype('float')
        summarydf2['Max Price'] = summarydf2['Max Price'].astype('float')
        summarydf2['Min Price'] = summarydf2['Min Price'].astype('float')
        
    sum_df_html = summarydf2
    
    return sum_df_html 

    
    
# =============================================================================
#     #==============================================================================
#     # Write to excel
#     #==============================================================================
#     
#     if len(filtereddf2)>0:
#         excelwriter = pd.ExcelWriter('CMBX Parsed File - '+dt.datetime.today().strftime('%m-%d-%Y')+'.xlsx')
#         #summarydf.to_excel(excelwriter,'Summary of DTCC Canada Trades')
#         summarydf2.to_excel(excelwriter,'Summary of DTCC CFTC Trades')
#         #filtereddf.to_excel(excelwriter,'Data Canada Trades',index = False)
#         filtereddf2.to_excel(excelwriter,'Data CFTC Trades',index = False)
#         excelwriter.save()
#         excelwriter.close()
#     
#     #==============================================================================
#     # Login into my outlook and send email
#     #==============================================================================
#     
#     
#     olMailItem = 0x0
#     outlook = win32com.client.Dispatch("Outlook.Application")
#     newmail = outlook.CreateItem(olMailItem)
#     newmail.To = "hsantana@tolisadvisors.com; spuliafico@tolisadvisors.com; ebanks@tolisadvisors.com; tpangia@tolisadvisors.com; sparker@tolisadvisors.com; jrosato@tolisadvisors.com; bilany@tolisadvisors.com"
#     newmail.Subject = "Daily CMBX Update"
#     if len(filtereddf2) > 0:
#         newmail.HTMLBody = "Hi all, <br><br>Please see below for the CMBX Universe Summary from todays recorded DTCC Trades. Attached is the breakout of the below summary data in the Data of Parsed Trades tab.<br><br>DTCC CFTC Trades<br><br>" + summarydf2.to_html()
#         newmail.Attachments.Add(Source = r'C:\Users\santana\Tolis Advisors LP\Technology - Shared\Python Tools - SOP, Scripts, Data\Data\CMBX Daily Update Data' +'\CMBX Parsed File - '+dt.datetime.today().strftime('%m-%d-%Y')+'.xlsx')
#         newmail.Send()
#     
# 
# =============================================================================
