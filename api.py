# import Session from the snowflake.snowpark package
from snowflake.snowpark import Session
# create a dictionary with the connection parameters
connection_parameters_dict = {
    "account": "MTLPIOD-XTC20354", # replace with your Snowflake account
    "user": "Intimatik", # replace with your username
    "password": "aZ5^YP$kuKtP$bB3", # replace with your password
    "role": "SYSADMIN",
    "warehouse": "BAKERY_WH",
    "database": "BAKERY_DB",
    "schema": "ORDERS"
}
# create the session object
my_session = Session.builder.configs(connection_parameters_dict).create()
# select the current timestamp
# ts = my_session.sql("select current_timestamp()").collect()
ts = my_session.sql("select delivery_date, baked_good_type, sum(quantity) as total_quantity from CUSTOMER_ORDERS group by all;").collect()
# print the output to the console
print(ts)
# close the session
my_session.close()