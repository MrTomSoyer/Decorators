import inspect
from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        date = datetime.now()
        result = old_function(*args, **kwargs)

        sig = inspect.signature(old_function)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        log_message = (
            f'Дата и время вызова функции: {date}\n'
            f'Имя функции: {old_function.__name__}\n'
            f'Аргументы (с учётом значений по умолчанию): {bound_args.arguments}\n'
            f'Возвращаемое значение: {result}\n\n'
        )

        with open('reg_exp.log', 'a', encoding='utf-8') as f:
            f.write(log_message)

        return result

    return new_function


def logger_with_params(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            date = datetime.now()
            result = old_function(*args, **kwargs)

            sig = inspect.signature(old_function)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            log_message = (
                f'Дата и время вызова функции: {date}\n'
                f'Имя функции: {old_function.__name__}\n'
                f'Аргументы (с учётом значений по умолчанию): {bound_args.arguments}\n'
                f'Возвращаемое значение: {result}\n\n'
            )

            with open(path, 'a', encoding='utf-8') as f:
                f.write(log_message)

            return result

        return new_function

    return __logger

