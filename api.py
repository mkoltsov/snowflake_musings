# import Session from the snowflake.snowpark package
from snowflake.snowpark import Session
# create a dictionary with the connection parameters
connection_parameters_dict = {

    "role": "SYSADMIN",
    "warehouse": "BAKERY_WH",
    "database": "BAKERY_DB",
    "schema": "SNOWPARK"
}
# create the session object
my_session = Session.builder.configs(connection_parameters_dict).create()
# select the current timestamp
ts = my_session.sql("select current_timestamp()").collect()
# print the output to the console
print(ts)
# close the session
my_session.close()