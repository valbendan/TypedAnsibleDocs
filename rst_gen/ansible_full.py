import os
import sys

from .j2_utils import render_jinja2_file

__all__ = ["gen_ansible_full"]

p_dir = os.path.dirname(__file__)


def gen_ansible_full(version: str):
    doc_dir = os.path.join(p_dir, f"../docs/ansible/{version}")
    if not os.path.isdir(doc_dir):
        sys.stderr.write(f"{doc_dir=} 不是有效的目录")
        sys.exit(2)

    doc_files = os.listdir(doc_dir)

    context = dict(version=version, doc_files=doc_files)

    rst_content = render_jinja2_file(os.path.join(p_dir, "ansible_full.jinja2"), context)

    with open(os.path.join(p_dir, f"../source/ansible/{version}.rst"), 'w') as fp:
        fp.write(rst_content)
