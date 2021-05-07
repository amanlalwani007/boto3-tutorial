import boto3

def dynamodb_createtable():
    dynamodb= boto3.resource('dynamodb')
    table= dynamodb.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName':'username',
                'KeyType':'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName':'username',
                'AttributeType':'S'
            },
            {
                'AttributeName':'last_name',
                'AttributeType':'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits':5,
            'WriteCapacityUnits':5
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName='users')
    print(table.item_count)


def table_creation_time():
    dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('users')
    print(table.creation_date_time)
    print(table.table_status )

def insert_data():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    table.put_item(Item={
        'username':'alalwan007',
        'first_name':'prem',
        'last_name':'lalwani',
        'age':21,
        'account_type':'standard_user'
        })
def get_item():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response =table.get_item(
        Key= {
            'username':'alalwani007',
            'last_name':'lalwani'
        })
    item=response['Item']
    print(item)

def updating_item():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    table.update_item(
        Key={
            'username':'alalwani007',
            'last_name':'lalwani'
        },
        UpdateExpression='SET age= :val1',
        ExpressionAttributeValues={
            ':val1':26
        }
    )


def scanning_and_query():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    from boto3.dynamodb.conditions import Key,Attr
    response= table.query(
        KeyConditionExpression=Key('username').eq('alalwani007')
    )
    items= response['Items']
    print(items)
    response=table.scan(
        FilterExpression=Attr('first_name').begins_with('A')&Attr('account_type').eq('super_user')
    )
    items=response['Items']
    print(items)

def table_delete():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    table.delete()


if __name__ == '__main__':
    #dynamodb_createtable()
    table_creation_time()
    #insert_data()
    #get_item()
    #updating_item()
    #get_item()
    # scanning_and_query()
    #https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Operations_Amazon_DynamoDB.html
