from decouple import config


ENV_POSSIBLE_OPTIONS = (
    "local",
    "prod",
)
ENV_ID = config("DJANGORLAR_ENV_ID", cast=str)
SECRET_KEY = 'django-insecure-4n(vsk0xjz7kw%7qk1q2h&n8d2q$cwo4%&_dc$%3^ka96t6#x0'