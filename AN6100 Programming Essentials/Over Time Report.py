import pandas as pd
import os
import datetime as dt

def VerifyDate(datastr):
    try:
        dt.datetime.strptime(datastr, '%Y-%m-%d')
        return True
    except:
        return False

def OverTimeReport():
    date = input('Please enter a date like 2021-05-04:')
    # prompt the user to enter the date he want to get the overtime report
    date = date.strip()
    if not VerifyDate(date):
        print(f"Please enter a valid date.")
        return 0
    # strip the space and check format of the input date
    year = date[0:4]
    month = date[5:7]
    filename = f'INOUT/MG_{year}{month}.csv'
    if os.path.exists(filename):
        pass
    else:
        print(f'Sorry, There is no {filename} in current working directory. \n'
              f'Please check your input or run option M first.')
        return 0
    # check whether there is the merged monthly file that option M generates
    df = pd.read_csv(filename, header=0)
    dfselectday = df.loc[df.Date == date, :]
    dfover9 = dfselectday.loc[dfselectday.Hrs >= 9, :]
    dfovertime = dfover9.loc[dfover9.Mins >= 15, :]
    # read the merged file as dataframe, select the date, sort out those who works over 9 hours 15 minutes.
    dfemployee =pd.read_csv('employees.csv', header=0)
    dfID = dfemployee.loc[:,['EmployeeID','TokenID']]
    tokentoemployee = {k:v for k,v in zip(dfID.loc[:,'TokenID'],dfID.loc[:,'EmployeeID'])}
    # read the employees data and then create a dictionary matching TokenID with corresponding EmployeeID.
    ovtime = pd.DataFrame(columns=['EmployeeID','Name','Work','Overtime in mins'])
    # create a empty dataframe ready to get overtime report data
    for i in dfovertime.loc[:,'Token ID']:
        newdata = dfemployee.loc[dfemployee.EmployeeID == tokentoemployee[i], ['EmployeeID','Name']]
        ovtime = ovtime.append(newdata, ignore_index=True,sort=False)
        # find those who works overtime on that day and match their TokenID with EmployeeID and name
        hour = int(dfovertime.loc[dfovertime['Token ID'] == i , 'Hrs'])
        mins = int(dfovertime.loc[dfovertime['Token ID'] == i , 'Mins'])
        ovtime.loc[ovtime.EmployeeID == tokentoemployee[i], 'Work'] = f'{hour}Hours{mins}Mins'
        overmins = (hour - 9) * 60 + mins
        ovtime.loc[ovtime.EmployeeID == tokentoemployee[i], 'Overtime in mins'] = overmins
        # calculate their work time and overtime, write the info into dataframe
    print(f'Over Time List For {date}')
    if ovtime.empty:
        print(f'No employee works overtime on {date}')
    else:
        print(ovtime)
    # print the overtime list from dataframe

if __name__ == "__main__":
    overtimereport()