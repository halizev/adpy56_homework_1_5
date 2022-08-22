import datetime


def parametrized_decorator(log_path='log_file.txt'):
    def homework_decorator(old_function):
        def wrapper(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(log_path, mode='a+', encoding='utf8') as f:
                f.write(f'Дата и время: {datetime.datetime.now()}\n')
                f.write(f'Название функции: {old_function.__name__}\n')
                f.write(f'Аргументы функции: {args, kwargs}\n')
                f.write(f'Результат функции: {result}\n')
            return result
        return wrapper
    return homework_decorator
