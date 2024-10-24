# download-aws-lambda-functions
A Python script to download the code of all AWS Lambda functions in your account, saving them locally as `.zip` files. This tool helps in backing up your Lambda function code and managing your AWS resources efficiently.



# AWS Lambda Code Downloader

This repository contains a Python script that downloads the code of all AWS Lambda functions in your AWS account and saves them locally in a specified directory. This can be useful for backing up Lambda function code or for version control.

## Features

- Lists all AWS Lambda functions in your account.
- Downloads the code of each function as a `.zip` file.
- Saves the downloaded files in a designated directory on your local machine.

## Requirements

- Python 3.x
- Boto3 library
- Requests library
