import os
import uuid

from .core import interactive, open_in_browser, ping, register_port, run, sub_parsers, threaded


STREAMLIT_PORT = 8501
register_port(STREAMLIT_PORT)


@interactive
def handler(parser_args, *args, **kwargs):
    if parser_args.no_browser is False:
        key = uuid.uuid4()
        url = f"http://localhost:{STREAMLIT_PORT}/"
        open_in_browser(url)

    script = parser_args.script
    if script != "hello":
        script = f"run {script}"

    return f"streamlit {script} --server.port={STREAMLIT_PORT} --server.address=0.0.0.0"


streamlit_parser = sub_parsers.add_parser("streamlit", help="Start streamlit server")
streamlit_parser.add_argument(
    "--no-browser", action="store_true", help="Don't open streamlit site in browser")
streamlit_parser.add_argument(
    "script",
    nargs="?",
    default="hello",
    help="Run your own script, defaults to hello example"
)
streamlit_parser.set_defaults(handler=handler)
