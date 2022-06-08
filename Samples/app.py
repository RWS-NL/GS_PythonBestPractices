# import config - settings
import config

# get db username
db_username = config.database['username']
print(f'db username: {db_username}')

# get db password
db_password = config.database['password']
print(f'db password: {db_password}')