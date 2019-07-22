import pandas as pd
import requests
import sys
import os

store_name = null
api_key = null
api_password = null

def main(data):

	if "Id" not in data.columns:
		print("Order ID not found in data")
	else:
		for ids in data['Id']:
			if not pd.isnull(ids):
				ids = str(int(ids))
				url = "https://%s:%s@%s.myshopify.com/admin/api/2019-04/orders/%s.json" %(api_key,api_password,store_name,ids)
				order_delete = requests.delete(url)
				print("Order with order id %s deleted successfully." %(str(int(ids))))
			else:
				print("Order ID not found")
		print("Total number of orders deleted : %s" %(len(data)))

if __name__ == '__main__':

	try:
		argv = sys.argv[1]
		if argv.endswith('.csv'):
			data = pd.read_csv(argv)
			main(data)
		elif argv.endswith('.xls') | argv.endswith('.xlsx'):
			data = pd.read_excel(argv)
			main(data)
		else:
			print("Wrong format file uploaded.PLease check the file format and upload again")
	except:				
			print("No input recieved. Please enter a file path")
