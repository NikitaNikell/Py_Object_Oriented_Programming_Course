# class Logger:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             _instance = super(Logger, cls).__new__(cls)
#             cls._instance.initialize_settings()
#             return _instance
#
#     def initialize_settings(self):
#         self.log_level = "INFO"
#
#     def set_level(self, value):
#         if self._instance:
#             self.log_level = value
#         else:
#             raise ValueError('The instance has not created')
#
#     @staticmethod
#     def get_logger(cls):
#         if _instance == None:


class Logger:
    _instance = None
    log_level = "INFO"

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    @classmethod
    def set_level(cls, new_level):
        if cls._instance is None:
            raise ValueError('The instance has not created')
        cls.log_level = new_level

    @staticmethod
    def get_logger():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance



logger_1 = Logger.get_logger()
print(logger_1.log_level)  # Выведет "INFO"
Logger.set_level("DEBUG")
print(logger_1.log_level)  # Выведет "DEBUG"

logger_2 = Logger.get_logger()
print(logger_2.log_level)  # Выведет "DEBUG"
print(logger_2 is logger_1)