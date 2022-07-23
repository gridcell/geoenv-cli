import uuid

from .core import interactive, open_in_browser, register_port, sub_parsers

JL_PORT = 8001
register_port(JL_PORT)


def handler(parser_args, *args, **kwargs):
    jl_key = ""
    if parser_args.no_browser is False:
        key = uuid.uuid4()
        jl_key = f"--NotebookApp.token='{key}'"
        url = f"http://localhost:{JL_PORT}/lab?token={key}"
        open_in_browser(url)

    interactive(
        lambda: f"python -m 'jupyterlab' {jl_key} --allow-root --port={JL_PORT} --ip=0.0.0.0"
    )()


jl_parser = sub_parsers.add_parser("jl", help="Start jupyter lab server")
jl_parser.add_argument(
    "--no-browser", action="store_true", help="Don't open Jupyter in browser"
)

jl_parser.set_defaults(handler=handler)
