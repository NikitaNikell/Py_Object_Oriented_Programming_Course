class AppSettings:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(AppSettings, cls).__new__(cls)
            # Логика инициализации настроек (может быть сложной)
            cls.__instance.initialize_settings()
        return cls.__instance

    def initialize_settings(self):
        # Логика инициализации настроек
        self.app_name = "MyApp 1.0"
        self.debug_mode = False
        self.log_level = "INFO"

    @staticmethod
    def get_app():
        if not AppSettings.__instance:
            AppSettings.__new__(AppSettings)
        return AppSettings.__instance


# Пример использования
app_settings_1 = AppSettings().get_app()
app_settings_2 = AppSettings()

print(app_settings_1 is app_settings_2)  # Выведет True

# Обращение к настройкам
print(app_settings_1.app_name)  # Выведет "MyApp"
print(app_settings_2.app_name)  # Выведет "MyApp"
print(app_settings_1.debug_mode)  # Выведет False
print(app_settings_2.debug_mode)  # Выведет False


print(app_settings_1.log_level)
