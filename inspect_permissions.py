import inspect
from importlib import import_module

import yaml


def list_module_classes(module_name):
    classes = []
    module = import_module(module_name)
    for name, item in inspect.getmembers(module):
        if inspect.isclass(item):
            classes.append(item)

    return classes


def parse_docstring(doc):
    """ 从注释中获取权限控制dict
    ...
    ---
    Permission:
        banner: 兑换码
        resource: redeem_code
        ction: create_redeem
        label: 创建兑换码
    ---
    ...
    """
    doc = doc.split('---')[1].split('--')[0]
    permission = yaml.load(doc)
    return permission


def collect_class_permissions(cls, decorator):
    lines = inspect.getsourcelines(cls)[0]
    lines = [line.strip() for line in lines if line.strip()]

    permissions = []
    with_decorator = False
    for line in lines:
        if line.startswith('@'):
            if line.split('(')[0] == '@' + decorator:
                with_decorator = True
        if line.startswith('def') and with_decorator:
            name = line.split('def')[1].split('(')[0].strip()
            doc = inspect.getdoc(getattr(cls, name))
            rv = parse_docstring(doc)
            if rv:
                permissions.extend(rv.values())

            with_decorator = False

    return permissions


def collect_permissons(module_name, decorator='permission_required'):
    classes = list_module_classes(module_name)
    permissions = []
    for cls in classes:
        permissions.extend(collect_class_permissions(cls, decorator))

    return permissions


if __name__ == "__main__":
    permissions = collect_permissons('handlers')
    for p in permissions:
        print(p)
