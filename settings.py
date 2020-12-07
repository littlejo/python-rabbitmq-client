protocol = 'amqps' #amqps or amqp
user = 'user'
password = 'password'
host = 'hostname'
port = '5671' #default port for amqps (5672 for amqp)

raw_url = f'{protocol}://{user}:{password}@{host}:{port}'
