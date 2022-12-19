# Robobarista

## Simple serverless app deployed with AWS SAM

This SAM application show a simple serverless coffee ordering app.
It should NOT be used in a production environment as it exposes an HTTP API endpoint from AWS API Gateway

```mermaid
flowchart LR;
    API-Gateway-->Lambda;
    Lambda-->DynamoDb;
```

Pre-requisites:
- Git client (https://github.com/git-guides/install-git)
- AWS CLI (https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- AWS SAM (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

Recommendation:
- Python 3.9


## Installing the coffee app

In your local dev folder clone the repository.
This will create a new folder call robobarista.

    git clone https://github.com/sosueme99/robobarista.git

    cd robobarista

    aws deploy --guided

The first time you run **sam deploy --guided** it will prompt for a few requirements.

You can save your choices in **samconfig.toml** file. 

You must specify Stack Name: The API Gateway, Lambda function and DynamoDb table will use this name.

Choose your region. Currently defaults to eu-west-2 London.

You will need to allow the SAM CLI IAM Role creation.

As this is just for short term demo we will not use an authoriser. Read more here about authorisers and access control. https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html 

Example output:

    Stack Name [sam-app]: your_app_name 
    AWS Region [eu-west-2]: 
    Confirm changes before deploy [y/N]: y
    Allow SAM CLI IAM role creation [Y/n]: y
    Disable rollback [y/N]: n
    LambdaFunction may not have authorization defined, Is this okay? [y/N]: y
    Save arguments to configuration file [Y/n]: y

## Updating the existing deployment
If you update the lambda or the SAM templates you can update the running application.

Run the following commands from the application folder

    sam build
    sam deploy

## Deleting the application
If you want to delete the application from your AWS account.

Run the following commands from the application folder

    sam delete




