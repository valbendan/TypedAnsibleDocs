import typer

app = typer.Typer()

from rst_gen.ansible_full import do_gen_ansible_full
from rst_gen.ansible_collection import do_gen_ansible_collection


@app.command()
def gen_ansible_full(version: str = typer.Argument("v5.3", help="生成 Ansible 版本的文档")):
    """
    生成 Ansible 指定版本的全部文档

    version 目录应该存在: docs/ansible/{version}
    """
    do_gen_ansible_full(version=version)


@app.command()
def gen_collection(name: str = typer.Argument(..., help="Ansible Collections 名称")):
    """
    生成 Ansible Collections 所有版本的文档

    name 目录应该存在: docs/{name}/
    """
    do_gen_ansible_collection(name=name)


if __name__ == "__main__":
    app()
