import os
import sys

__all__ = ["do_gen_ansible_collection"]

from .j2_utils import render_jinja2_file

p_dir = os.path.dirname(__file__)


def do_gen_ansible_collection(name: str):
    collection_dir = os.path.join(p_dir, f"../docs/{name}")
    if not os.path.isdir(collection_dir):
        sys.stderr.write(f"{collection_dir=} is not valid directory")
        sys.exit(2)

    version_list = os.listdir(collection_dir)

    context = dict(name=name, version_list=version_list)

    rst_content = render_jinja2_file(
        os.path.join(p_dir, "ansible_collection.jinja2"), context
    )

    with open(os.path.join(p_dir, f"../source/collections/{name}.rst"), "w") as fp:
        fp.write(rst_content)
