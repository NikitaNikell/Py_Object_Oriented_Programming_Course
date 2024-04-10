class BaseConfig:
    def __new__(cls, *args, **kwargs):
        instance = super(BaseConfig, cls).__new__(cls)
        instance.debug = False
        instance.log_level = "INFO"
        return instance


class EmailConfig(BaseConfig):

    def __new__(cls, *args, **kwargs):
        instance = BaseConfig()
        instance.smtp_server = "smtp.gmail.com"
        instance.smtp_port = "587"
        instance.username = "boss_of_gym@gmail.com"
        instance.password = ""
        return instance


class DatabaseConfig(BaseConfig):

    def __new__(cls, *args, **kwargs):
        instance = BaseConfig()
        instance.db_host = '127.0.0.1'
        instance.db_port = '5432'
        instance.db_name = 'cookies'
        instance.db_user = 'admin'
        instance.db_password = 'admin'
        return instance




database_config = DatabaseConfig()

print("Database Configuration:")
print(f"Host: {database_config.db_host}")
print(f"Port: {database_config.db_port}")
print(f"Database name: {database_config.db_name}")
print(f"User: {database_config.db_user}")
print(f"Password: {database_config.db_password}")
print(f"Debug: {database_config.debug}")
print(f"Logger: {database_config.log_level}")



