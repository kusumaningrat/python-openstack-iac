# from openstack import connection


# conn = connection.Connection(
#     auth_url='http://192.168.56.56:5000/v3',
#     project_name='admin',
#     username='admin',
#     password='admin',
#     user_domain_name='default',
#     project_domain_name='default'
# )

# images = conn.image.images()

# for image in images:
#     print("Name:", image.name)
#     print("ID:", image.id)

# from dotenv import load_dotenv
# import os

# load_dotenv()

# auth = os.getenv('AUTH_URL')

# print(auth)

def my_function(arg1, arg2, **kwargs):
    print('arg1:', arg1)
    print('arg2:', arg2)
    for key, value in kwargs.items():
        print(key, ':', value)