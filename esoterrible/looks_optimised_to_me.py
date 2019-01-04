import inspect
import time

ACCEPTABLE_FUNCTION_LENGTH = 20

time_sleep = time.sleep


def scaling_sleep(secs):
    # Inspecting the stack to retrieve the source code of the function/module where this was called
    caller_source = inspect.getsourcelines(inspect.stack()[1][0])[0]

    superfluous_space = len([line for line in caller_source if len(line.strip()) == 0]) / len(caller_source)
    long_function_multiplier = max(len(caller_source), ACCEPTABLE_FUNCTION_LENGTH) / ACCEPTABLE_FUNCTION_LENGTH

    secs = secs * (1 + superfluous_space) * long_function_multiplier
    return time_sleep(secs)


time.sleep = scaling_sleep
