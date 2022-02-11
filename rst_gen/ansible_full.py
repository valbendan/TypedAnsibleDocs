import os
import sys
from functools import cmp_to_key

from packaging.version import parse

from .j2_utils import render_jinja2_file

__all__ = ["do_gen_ansible_full"]

p_dir = os.path.dirname(__file__)


def _version_cmp(v1, v2):
    return parse(v1) < parse(v2)


def do_gen_ansible_full(version: str):
    doc_dir = os.path.join(p_dir, f"../docs/ansible/{version}")
    if not os.path.isdir(doc_dir):
        sys.stderr.write("doc_dir=" + doc_dir + " 不是有效的目录")
        sys.exit(2)

    doc_files = sorted(os.listdir(doc_dir), key=cmp_to_key(_version_cmp))

    context = dict(version=version, doc_files=doc_files)

    rst_content = render_jinja2_file(
        os.path.join(p_dir, "ansible_full.jinja2"), context
    )

    with open(os.path.join(p_dir, f"../source/ansible/{version}/index.rst"), "w") as fp:
        fp.write(rst_content)
