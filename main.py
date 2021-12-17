from Classes.enviromesh_logger import *


# TODO: Loop readings with 15 second time.sleep
# TODO: Implement AWS IOT CORE Publish DATA
# * ^When publishing add timestamp as well

# TODO: Implement AWS IOT RULE to trigger An AWS Lambda
# TODO: AWS Lambda will take the data as an object and interact with our AWS RDS_SQL
if __name__ == '__main__':
    Env_logger = Enviromesh_logger()
