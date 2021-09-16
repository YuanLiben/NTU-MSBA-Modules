# Web Assignment Part 2/2
# Date:     2021 Aug 08
# Author:   Yuan Liben
# Group:    B
# Index Number: 43
# Organisation: Nanyang Business School, NTU
# Program:  MSBA
# Course:   AN6100-Programming Essentials
# --------------------------------------------
from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

# Define the original dataframe and store it to the csv file.
app = Flask(__name__)
api = Api(app)

df = pd.DataFrame({'ID': [1001, 1002, 1003, 1004, 1005],
                   'Name': ['Noel', 'Luke', 'Sirius', 'Simon', 'Benjamin']})
df.to_csv('customers.csv', index=False)
df = pd.read_csv('customers.csv')


# Print the class group, index number and name of the author.
class Author(Resource):
    def get(self):
        return 'Class Group: B, Index Number: 43, Name: Yuan Liben'


# Display all the customers present in the dataframe.
class Display(Resource):
    def get(self):
        dfdict = df.to_dict('records')
        return dfdict


# Get the input id from url and check whether it is in the customer id list. If yes
# then print the name of the customer with this id. If no, return a notice.
class Search(Resource):
    def get(self):
        idlist = df.loc[:, 'ID']
        idlist = idlist.to_list()
        idinput = int(request.args.get('id'))
        if idinput in idlist:
            targetname = df.loc[df.ID == idinput, 'Name']
            targetname = targetname.to_string(index=False)
            return targetname
        else:
            return f'There is no customer with ID {idinput}.'


# Get the input id and name from url and check whether the id is in the current customer
# id list. If yes return a notice. If no then add the new customer into dataframe as well
# as store it to the csv file.
class Add(Resource):
    def get(self):
        global df
        idlist = df.loc[:, 'ID']
        idlist = idlist.to_list()
        idinput = int(request.args.get('id'))
        nameinput = request.args.get('name')
        if idinput not in idlist:
            df = df.append({'ID': idinput, 'Name': nameinput}, ignore_index=True)
            df.to_csv('customers.csv', index=False)
            return 'New customer created!'
        else:
            return f'ID {idinput} is already occupied, please use a different ID.'


# Add the corresponding URL endpoints.
api.add_resource(Author, '/')
api.add_resource(Display, '/b/customer/all')
api.add_resource(Search, '/b/customer')
api.add_resource(Add, '/b/customer/add')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)
