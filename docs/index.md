# Command Line Interface Docs

This python module is used to make your command line / terminal more fancy when printing / logging certain events.

## Table of contents
- [Command Line Interface Docs](#command-line-interface-docs)
  - [Table of contents](#table-of-contents)
  - [Quick install](#quick-install)
  - [Functions](#functions)
    - [cli.info()](#cliinfo)
    - [cli.debug()](#clidebug)
    - [cli.warn()](#cliwarn)
    - [cli.error()](#clierror)
    - [cli.add()](#cliadd)
    - [cli.init()](#cliinit)
  - [Colors](#colors)
  - [Examples](#examples)
    - [Basic usage](#basic-usage)
    - [Advanced usage](#advanced-usage)

## Quick install

```bash
pip install cli-log
```

## Functions

### [cli.info()](https://github.com/DeltaBotics/cli-log/blob/bc0dc4f66d6df40b92f714fd92b5db1f4d20801a/cli/core.py#L24-L37)

Usage : ``cli.info(message, prefix='', color=cli.Blue')``

`message` : `str` 
The message to log.
`prefix` : `str`, (optional)
An optional prefix for the log message. Defaults to `''`.
`color` : `str`, optional
An optional color for the log message. Defaults to `BLUE`.

### [cli.debug()](https://github.com/DeltaBotics/cli-log/blob/bc0dc4f66d6df40b92f714fd92b5db1f4d20801a/cli/core.py#L39-L52)

Usage : ``cli.debug(message, prefix='', color=cli.GREEN)``

`message` : `str` 
The message to log.
`prefix` : `str`, (optional)
An optional prefix for the log message. Defaults to `''`.
`color` : `str`, (optional)
An optional color for the log message. Defaults to `GREEN`.

### [cli.warn()](https://github.com/DeltaBotics/cli-log/blob/bc0dc4f66d6df40b92f714fd92b5db1f4d20801a/cli/core.py#L54-L67)

Usage  : ``cli.warn(message, prefix='', color=cli.YELLOW)``

`message` : `str` 
The message to log.
`prefix` : `str`, (optional)
An optional prefix for the log message. Defaults to `''`.
`color` : `str`, (optional)
An optional color for the log message. Defaults to `YELLOW`.

### [cli.error()](https://github.com/DeltaBotics/cli-log/blob/bc0dc4f66d6df40b92f714fd92b5db1f4d20801a/cli/core.py#L69-L83)

Usage : ``cli.error(message, prefix='', color=cli.RED)``

`message` : `str` 
The message to log.
`prefix` : `str`, (optional)
An optional prefix for the log message. Defaults to `''`.
`color` : `str`, (optional)
An optional color for the log message. Defaults to `RED`.

### [cli.add()](https://github.com/DeltaBotics/cli-log/blob/bc0dc4f66d6df40b92f714fd92b5db1f4d20801a/cli/core.py#L6-L22)

Usage  : ``cli.add(severity, message, prefix='', color=cli.WHITE)``

`severity` : `str` 
The severity of the log message.
`message` : `str` 
The message to log.
`prefix` : `str`, (optional)
An optional prefix for the log message. Defaults to `''`.
`color` : `str` 
An optional color for the log message. Defaults to `WHITE`.

### [cli.init()](https://github.com/DeltaBotics/cli-log/blob/bc0dc4f66d6df40b92f714fd92b5db1f4d20801a/cli/__init__.py#L3)


Usage to set log_format : ``cli.init(prefix='[{time} / {severity}]{prefix} {message}')``
Usage to reset log_format : ``cli.init(reset=True)``

`log_format` : `str`, (optional)
The format of the log messages. Defaults to `'[{time} / {severity}]{prefix} {message}'`.
`reset` : `bool`, (optional)
Whether or not to reset the `log_format` to the default. Defaults to `False`.

## Colors
**BLUE** is the default color for [cli.info()](#cliinfo), set it using `cli.BLUE`.
**GREEN** is the default color for [cli.debug()](#clidebug), set it using `cli.GREEN`.
**YELLOW** is the default color for [cli.warn()](#cliwarn), set it using `cli.YELLOW`.
**RED** is the default color for [cli.error()](#clierror), set it using `cli.RED`.
**WHITE** is the default color for [cli.add()](#cliadd), set it using `cli.WHITE`.
**MAGENTA**, set it using `cli.MAGENTA`.
**CYAN**, set it using `cli.CYAN`.
**BLACK**, set it using `cli.BLACK`.

> [!TIP]
> The colors can also be set using [colorama](https://github.com/tartley/colorama?tab=readme-ov-file#colored-output).
> Or you can use your own [ANSI](https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007#file-colors-py) sequences.

## Examples

### Basic usage
```python
import cli

cli.info("Hello world!\nInfo event.")
cli.debug("Debug event.")
cli.warn(prefix="CORE", message="Warning event.")
cli.error("Error event.")
```

```log
[16:30:52 / INFO] Hello world!
[16:30:52 / INFO] Info event.
[16:30:52 / DEBUG] Debug event.
[16:30:52 / WARN][CORE] Warning event.
[16:30:52 / ERROR] Error event.
```

### Advanced usage
```python
import cli

cli.info("Hello world!")
cli.add(severity="Testing", message="Hello", prefix="test", color=cli.MAGENTA)
cli.init(log_format="[{time} ! {severity}]{prefix} {message}", reset=True)
cli.error("Error between error raising.")
cli.init(reset=True) # Doesn't do anything because we didnt set format before
cli.debug("Should not get executed.")
cli.init(log_format="[{severity} ! {time}]{prefix} {message}")
cli.info(message="Hello", color=cli.BLACK)
```

```log
[16:30:52 / INFO] Hello world!
[16:30:52 / TESTING][test] Hello
Traceback (most recent call last):
    File "usr/local/lib/python3.11/site-packages\cli-log\initialise.py", line 18, in init
        raise ValueError("Cannot use 'reset' parameter in combination with 'log_format'")
ValueError: Cannot use 'reset' parameter in combination with 'log_format'

[16:30:52 ! ERROR] Error between error raising.
[16:30:52 / DEBUG] Should not get executed.
[16:30:52 ! INFO] Hello
```
Here you can see that an error was raised due to the usage of the `reset` parameter in combination with the `log_format` parameter.

You can also see that the `[16:30:52 / DEBUG]` is not using `[16:30:52 ! DEBUG]` because the format was reset.