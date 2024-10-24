import boto3
import os
import requests

client = boto3.client('lambda')

# Directory to save all the lambda functions' code
download_dir = './lambda_functions_code'

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

def download_lambda_function(function_name):
    try:
        response = client.get_function(FunctionName=function_name)
        code_url = response['Code']['Location']

        code_zip_file = os.path.join(download_dir, f"{function_name}.zip")
        r = requests.get(code_url)
        if r.status_code == 200:
            with open(code_zip_file, 'wb') as file:
                file.write(r.content)  
            print(f"Downloaded code for {function_name}")
        else:
            print(f"Failed to download code for {function_name}: HTTP {r.status_code}")
    
    except Exception as e:
        print(f"Failed to download code for {function_name}: {str(e)}")

def download_all_functions():
    paginator = client.get_paginator('list_functions')
    for page in paginator.paginate():
        functions = page['Functions']
        for function in functions:
            function_name = function['FunctionName']
            download_lambda_function(function_name)

if __name__ == "__main__":
    download_all_functions()
