from openstack import connection

def create_connection(auth_url, project_name, username, password, user_domain_name, project_domain_name):
    return connection.Connection(
        auth_url=auth_url,
        project_name=project_name,
        username=username,
        password=password,
        user_domain_name=user_domain_name,
        project_domain_name=project_domain_name
    )

def get_connection():
    with open('.env') as file:
        env_vars = dict(line.strip().split('=') for line in file)

    conn = create_connection(
        auth_url=env_vars['AUTH_URL'],
        project_name=env_vars['PROJECT_NAME'],
        username=env_vars['USERNAME'],
        password=env_vars['PASSWORD'],
        user_domain_name=env_vars['USER_DOMAIN_NAME'],
        project_domain_name=env_vars['PROJECT_DOMAIN_NAME']
    )
    return conn

