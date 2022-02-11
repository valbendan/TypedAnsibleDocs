import os
import sys

__all__ = ["do_gen_ansible_collection"]

from .j2_utils import render_jinja2_file

p_dir = os.path.dirname(__file__)


def do_gen_ansible_collection(name: str):
    collection_dir = os.path.join(p_dir, "../docs/{name}".format(name=name))
    if not os.path.isdir(collection_dir):
        sys.stderr.write(
            "collection_dir={collection_dir} is not valid directory".format(
                collection_dir=collection_dir
            )
        )
        sys.exit(2)

    version_list = reversed(sorted(os.listdir(collection_dir)))

    context = dict(name=name, version_list=version_list)

    rst_content = render_jinja2_file(
        os.path.join(p_dir, "ansible_collection.jinja2"), context
    )

    index_dir = os.path.join(p_dir, f"../source/collections/{name}")
    if not os.path.isdir(index_dir):
        os.mkdir(index_dir, 0o775)

    with open(os.path.join(index_dir, "index.rst"), "w") as fp:
        fp.write(rst_content)
