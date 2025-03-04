import click
import sys 


from loguru import logger


from xarxes2025.server import Server
from xarxes2025.client import Client


@click.group()
@click.version_option()
@click.option('--debug/--no-debug', default=False,show_default=True)
@click.option('--debug-level', default='INFO',show_default=True,
              type=click.Choice(['TRACE', 'DEBUG', 'INFO', 'WARNING', 'ERROR'], case_sensitive=False))
@click.option('--debug-file/--no-debug-file', default=False,show_default=True)
@click.option('--debug-filename', type=click.Path(),show_default=True, default="xarxes.log")
@click.pass_context
def cli(ctx, debug, debug_level, debug_file, debug_filename):
    """
    Main entry point for the CLI.

    This function sets up the Click CLI group, and adds options for
    debugging. The `debug` option enables debug logging, and the
    `debug-level` option sets the level of debug logging. The
    `debug-file` option sets the file where logs are written.

    The function also sets up the logging format and level based on the
    options provided. If file logging is enabled, the function sets up
    both console and file logging; otherwise, only console logging is
    enabled.
    """
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug
    ctx.obj['DEBUG_LEVEL'] = debug_level
    ctx.obj['DEBUG_FILE'] = debug_file
    fmt = "<e>{file}</e> | <r>{line}</r> | <g>{time:DD/MM/YY HH:mm:ss:SSS}</> | <lvl>{level}</> | <c>{message}</>"
    if not debug_file:
            debug_filename = sys.stderr
    if debug:
        if debug_level in ["TRACE", "DEBUG", "INFO", "WARNING", "ERROR"]:
            logger.remove(0)
            # logger.add(sys.stderr, level= debug_level, format=fmt, colorize=True)
            logger.add(debug_filename, level= debug_level, format=fmt, colorize=True)
        else:
            logger.remove(0)            
            logger.add(debug_filename, level="ERROR", format=fmt, colorize=True)
    else:
        logger.remove(0)
        logger.add(sys.stderr, level="ERROR", format=fmt, colorize=True)

    logger.debug(f"Debug mode is {'on' if debug else 'off'}")
    logger.debug(f"Debug level is {debug_level}")
    logger.debug(f"Debug file is {debug_file}")


@cli.command(name="server")
@click.pass_context
@click.option(
    "-p",
    "--port",
    help="RTSP port (TCP)",
    default=4321,
    show_default=True,
    type=int
)
def server(ctx, port):
    """
    Start an RTSP server streaming video.

    \b
    The server will listen for incoming RTSP connections on the specified
    port (default is 4321).
    """
    logger.info("Server xarxes 2025 video streaming")
    server = Server(port)


@cli.command(name="client")
@click.pass_context
@click.argument("videofile", 
    type=click.Path(), 
    required=False, 
    default="rick.webm"
)
@click.option(
    "-p",
    "--port",
    help="RTSP port (TCP)",
    default=4321,
    show_default=True,
    type=int
)
def client(ctx, videofile, port):
    """
    Start an RTSP client streaming video.

    \b
    The client will use for outgoing RTSP connections the specified
    port (default is 4321).
    """
    logger.info("Client xarxes 2025 video streaming")
    client = Client(port, videofile)
    client.root.mainloop()
