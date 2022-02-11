from jinja2 import Environment, BaseLoader

__all__ = ["render_jinja2_file"]


def render_jinja2_file(file: str, ctx: dict) -> str:
    """
    Render specify jinja2 file with specify context

    :param file:  jinja2 template file
    :param ctx:  render context
    :return:
    """
    with open(file) as fp:
        tpl = Environment(loader=BaseLoader()).from_string(fp.read())
        return tpl.render(**ctx)
