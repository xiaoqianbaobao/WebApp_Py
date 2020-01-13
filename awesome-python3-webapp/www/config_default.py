"""
Default configurations.
"""
#开发环境标准配置
configs = {
    'debug': True,
    'db': {
        'host': "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "csq123",
        "db": 'awesome'
    },
    "session": {
        "secret": 'MyBlog'
    }
}