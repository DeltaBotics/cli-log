import os
import logging as real_logging # Real logging package
from . import levels as logging # Custom logging package
from logging.handlers import SysLogHandler
from logging import StreamHandler

class OverwriteFileHandler(real_logging.FileHandler):
    def __init__(self, filename, mode='a', encoding=None, delay=False, maxBytes=0, backupCount=0):
        if mode == 'w':
            # Ensure the file is created in write mode, overwriting any existing content
            if os.path.isfile(filename):
                open(filename, 'w').close()  # Truncate the file if it exists
        super().__init__(filename, mode, encoding, delay)
        self.maxBytes = maxBytes
        self.backupCount = backupCount
        if maxBytes > 0:
            self.mode = 'w'

    def emit(self, record):
        """
        Emit a log record.
        """
        if self.shouldRollover(record):
            self.rollOver()
        real_logging.FileHandler.emit(self, record)

    def shouldRollover(self, record):
        if self.maxBytes > 0:  # are we rolling over?
            msg = "%s\n" % self.format(record)
            self.stream.seek(0, 2)  # due to non-posix-compliant Windows feature
            if self.stream.tell() + len(msg) >= self.maxBytes:
                return True
        return False

    def rollOver(self):
        if self.backupCount > 0:
            for i in range(self.backupCount - 1, 0, -1):
                sfn = "%s.%d" % (self.baseFilename, i)
                dfn = "%s.%d" % (self.baseFilename, i + 1)
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.remove(dfn)
                    os.rename(sfn, dfn)
            dfn = self.baseFilename + ".1"
            if os.path.exists(dfn):
                os.remove(dfn)
            os.rename(self.baseFilename, dfn)
        if self.mode == 'w':
            self.stream.seek(0, 2)  # due to non-posix-compliant Windows feature
        self.mode = 'w'
        self.stream.truncate()
        self.stream.seek(0, 0)

def init(
        level = logging.DEBUG,
        handler_type = 'syslog',
        facility = SysLogHandler.LOG_DAEMON,
        address = '/dev/log',
        log_file_path = None,
        mode = 'a',
        max_bytes = 10485760,
        backup_count = 5,
        stream = None,
        fmt="%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d %(levelname)s - '%(message)s'",
        datefmt="%Y-%m-%d %H:%M:%S"
        ) -> None:

    """
    Initialises the logging system with the specified options.

    Parameters
    ----------
    `level` : :class:`int`, optional
        The logging level (e.g., `logging.DEBUG`, `logging.INFO`). Defaults to `logging.DEBUG`.
    `handler_type` : :class:`str`, optional	
        Type of logging handler (`'syslog'`, `'file'`, `'stream'`). Defaults to `'syslog'`.
    `facility` : :class:`int`, optional
        Syslog `facility` if `handler_type` is 'syslog'. Defaults to `SysLogHandler.LOG_DAEMON`.
    `address` : :class:`str`, optional
        Address for syslog logging if `handler_type` is 'syslog'. Defaults to `'/dev/log'`.
    `log_file_path` : :class:`str`, optional
        Path to the log file if `handler_type` is `'file'`. Required if `handler_type` is `'file'`.
    `mode` : :class:`str`, optional
        Mode for opening the log file if `handler_type` is `'file'`. Defaults to `'a'` (append mode).
    `max_bytes` : :class:`int`, optional
        Maximum size of the log file before rotation (used with `'file'` handler). Defaults to `10485760` bytes (10 MB).
    `backup_count` : :class:`int`, optional
        Number of backup log files to keep (used with `'file'` handler). Defaults to `5`.
    `stream` : :class:`file-like object`, optional
        Stream to log to if `handler_type` is `'stream'` (e.g., `sys.stdout`). Defaults to `None`.
    `fmt` : :class:`str`, optional
        Log message format. Defaults to `"%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d %(levelname)s - '%(message)s'"`.
    `datefmt` : :class:`str`, optional
        Date/time format for log messages. Defaults to `"%Y-%m-%d %H:%M:%S"`.
    """

    logger = real_logging.getLogger(__name__)
    logger.setLevel(level)

    if handler_type == 'syslog':
        if not hasattr(real_logging, 'SysLogHandler'):
            raise ValueError("Syslog logging is not supported on this platform.")
        handler = SysLogHandler(facility=facility, address=address)
    elif handler_type == 'file':
        if log_file_path is None:
            raise ValueError("log_file_path must be specified for file handler")
        elif mode is not None and mode not in ('a', 'w'):
            raise ValueError("mode must be one of 'a' (append), 'w' (write)")
        handler = OverwriteFileHandler(log_file_path, mode=mode, maxBytes=max_bytes, backupCount=backup_count)
    elif handler_type == 'stream':
        handler = StreamHandler(stream=stream)
    else:
        raise ValueError("Invalid handler_type specified. Choose 'syslog', 'file', or 'stream'.")

    formatter = real_logging.Formatter(fmt=fmt, datefmt=datefmt)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger