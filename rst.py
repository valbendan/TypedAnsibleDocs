import typer

app = typer.Typer()

from rst_gen.ansible_full import gen_ansible_full


@app.command()
def gen_ansible_full(version: typer.Argument("v5.3", help="生成 Ansible 版本的文档")):
    """
    生成 Ansible 指定版本的全部文档

    version 目录应该存在: docs/ansible/{version}
    """
    gen_ansible_full(version=version)


if __name__ == "__main__":
    typer.run(app)
