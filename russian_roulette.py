from cross_platform_shutdown import shutdown
from random import randint

if randint(1, 6) == 1:
    shutdown()
