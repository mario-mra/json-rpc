from .manager import JSONRPCResponseManager
from .dispatcher import Dispatcher

__version = (1, 13, 0)

__version__ = version = '.'.join(map(str, __version))
__project__ = PROJECT = __name__
__author__ = 'Kirill Pavlov (@pavlov99) <k@p99.io>'

dispatcher = Dispatcher()

# lint_ignore=W0611,W0401
