import json
import boto3
import random
import uuid
from datetime import datetime

# Modify the values below to match your dynamoDB table.
# The table should be in the same region as this lambda function. test
dynamodDBTablename = 'robobarista'
primarydbKey = 'orderID'
client = boto3.resource('dynamodb')
table = client.Table(dynamodDBTablename)

def lambda_handler(event, context):
    
    # Get order time from dateTime
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    available_coffees = ['americano','latte','cappuccino','espresso','machiato','caramel-latte','cortado']
    available_sizes = ['small','medium','regular','large','extra-large']
    available_milks = ['soya','semi','full','almond']
    
    #Generate UUID4 to be used as orderID partition key in the dynamodDB orders table
    orderID = str(uuid.uuid4())
    
    coffee_size = ""
    coffee_type = ""
    milk_type = ""
    
    # Check to see if approved coffee, size and milk have been passed
    # If nothing then a random coffee order is created.
    try:
        coffee_type = event['coffee_type']
        if coffee_type not in available_coffees:
            coffee_type = random.choice(available_coffees)
    except:
        coffee_type = random.choice(available_coffees)
            
    try:
        coffee_size = event['coffee_size']
        if coffee_size not in available_sizes:
            coffee_size = random.choice(available_sizes)
    except:
        coffee_size = random.choice(available_sizes)
    
    try:
        milk_type = event['milk_type']
        if milk_type not in available_milks:
            milk_type = random.choice(available_milks)
    except:
            milk_type = random.choice(available_milks)
        
    
    try :
        table.put_item(Item= {primarydbKey : orderID,'order_date':date_time_str,'coffee_type': coffee_type,'coffee_size': coffee_size,'milk_type': milk_type,'order_completed': 'false'})
    except :
        print("Unable to connect to database")
        return {
            'order_status': 400,
            'body': 'Unable to connect to dynamodDB'
        }    
    
    return {
        'order_status': 200,
        'body': 'Order added to dynamoDB'
    }
