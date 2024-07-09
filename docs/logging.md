This is the documentation for the built-in-logging functionality. <br />
Its a subclass of the standard logging library included in python. <br />

# Table of Contents
- [Table of Contents](#table-of-contents)
- [logging.init()](#logginginit)
- [Examples](#examples)

# [logging.init()](https://github.com/DeltaBotics/cli-log/blob/6f6db7af897652adc9a9d9f0f35c965737dd387e/cli/logging/initialise.py#L5-L59)
To enable the syslog, filelog or streamlog, call the logging.init() function with the appropriate parameters. <br />

Initialises the logging system with the specified options. <br />

`level` : `int`, (optional) <br />
The logging level (e.g., `logging.DEBUG`, `logging.INFO`). Defaults to `logging.DEBUG`. <br />
`handler_type` : `str`, (optional) <br />
Type of logging handler (`'syslog'`, `'file'`, `'stream'`). Defaults to `'syslog'`. <br />
`facility` : `int`, (optional) <br />
Syslog `facility` if `handler_type` is `'syslog'`. Defaults to `SysLogHandler.LOG_DAEMON`. <br />
`address` : `str`, (optional) <br />
Address for syslog logging if `handler_type` is 'syslog'. Defaults to `'/dev/log'`. <br />
`log_file_path` : `str`, (optional) <br />
Path to the log file if `handler_type` is `'file'`. Required if `handler_type` is `'file'`. <br />
`mode` : `str`, (optional) <br />
Mode for opening the log file if `handler_type` is `'file'`. Defaults to `'a'` (append mode). <br />
`max_bytes` : `int`, (optional) <br />
Maximum size of the log file before rotation (used with `'file'` handler). Defaults to `10485760` bytes (10 MB). <br />
`backup_count` : `int`, (optional) <br />
Number of backup log files to keep (used with `'file'` handler). Defaults to `5`. <br />
`stream` : `file-like object`, (optional) <br />
Stream to log to if `handler_type` is `'stream'` (e.g., `sys.stdout`). Defaults to `None`. <br />
`fmt` : `str`, (optional) <br />
Log message format. Defaults to `"%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d %(levelname)s - '%(message)s'"`. <br />
`datefmt` : `str`, (optional) <br />
Date/time format for log messages. Defaults to `"%Y-%m-%d %H:%M:%S"`. <br />

# Examples

```python
import cli

def test_logging():
    try:
        # Configure logging to a file
        cli.logging.init(level=cli.logging.DEBUG, mode='w', handler_type='file', log_file_path='testing/test.log')

        cli.info('CLI started\nYo')
        cli.warn('Sup')
        cli.debug('I am a debug')
        cli.critical('Critical')

    except Exception as e:
        print(f"Exception occurred: {str(e)}")

if __name__ == "__main__":
    test_logging()
```

Terminal output:
```log
[01:34:47 / INFO] CLI started
[01:34:47 / INFO] Yo
[01:34:47 / WARN] Sup
[01:34:47 / DEBUG] I am a debug
[01:34:47 / CRITICAL] Critical
```

File output under `testing/test.log`:
```log
2024-07-09 01:34:47 - core.py:log:120 INFO - 'CLI started'
2024-07-09 01:34:47 - core.py:log:120 INFO - 'Yo'
2024-07-09 01:34:47 - core.py:log:124 WARNING - 'Sup'
2024-07-09 01:34:47 - core.py:log:122 DEBUG - 'I am a debug'
2024-07-09 01:34:47 - core.py:log:128 CRITICAL - 'Critical'
```