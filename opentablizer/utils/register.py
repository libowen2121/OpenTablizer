import importlib
import inspect
from typing import List, Tuple, Union
from icecream import ic
from opentablizer.utils.config import ConfigDict

from opentablizer.utils.constants import DEFAULT_GROUP_NAME, TYPE


ALL_ENTITY_PIPELINES = [
    'named_entity_recognition',
]

# Pipelines to be imported
ALL_PIPELINES = [
    ('opentablizer.pipelines.entity', ALL_ENTITY_PIPELINES),
]

ALL_ENTITY_MODELS = [
    'hanlp_named_entity_recognition',
    'regex_named_entity_recognition'
]

# Models to be imported
ALL_MODELS = [
    ('opentablizer.models.entity', ALL_ENTITY_MODELS),
]


class Register(object):
    """Reigistry which supports registering modules and group them by a keyname
    If group name is not provided, modules will be registered to default group.
    """    

    def __init__(self, name: str):
        self._name = name
        self._modules = {DEFAULT_GROUP_NAME: {}}

    def __repr__(self):
        format_str = self.__class__.__name__ + f' ({self._name})\n'
        for group_name, group in self._modules.items():
            format_str += f'group_name={group_name}, '\
                f'modules={list(group.keys())}\n'

        return format_str

    @property
    def name(self):
        return self._name

    @property
    def modules(self):
        return self._modules

    # def list(self):
    #     """ logging the list of module in current registry
    #     """
    #     for group_name, group in self._modules.items():
    #         logger.info(f'group_name={group_name}')
    #         for m in group.keys():
    #             logger.info(f'\t{m}')
    #         logger.info('')

    def get(self, module_key, group_key=DEFAULT_GROUP_NAME):
        if group_key not in self._modules:
            return None
        else:
            return self._modules[group_key].get(module_key, None)

    def _register_module(self,
                         group_key=DEFAULT_GROUP_NAME,
                         module_name=None,
                         module_cls=None,
                         force=False):
        assert isinstance(group_key,
                          str), 'group_key is required and must be str'

        if group_key not in self._modules:
            self._modules[group_key] = dict()

        if not inspect.isclass(module_cls):
            raise TypeError(f'module is not a class type: {type(module_cls)}')

        if module_name is None:
            module_name = module_cls.__name__

        if module_name in self._modules[group_key] and not force:
            raise KeyError(f'{module_name} is already registered in '
                           f'{self._name}[{group_key}]')
        self._modules[group_key][module_name] = module_cls
        module_cls.group_key = group_key

    def register_module(self,
                        group_key: str = DEFAULT_GROUP_NAME,
                        module_name: str = None,
                        module_cls: type = None,
                        force=False):
        """ Register module

        Example:
            >>> models = Register('models')
            >>> @models.register_module('image-classification', 'SwinT')
            >>> class SwinTransformer:
            >>>     pass

            >>> @models.register_module('SwinDefault')
            >>> class SwinTransformerDefaultGroup:
            >>>     pass

            >>> class SwinTransformer2:
            >>>     pass
            >>> MODELS.register_module('image-classification',
                                        module_name='SwinT2',
                                        module_cls=SwinTransformer2)

        Args:
            group_key: Group name of which module will be registered,
                default group name is 'default' (Task)
            module_name: Module name (Pipeline)
            module_cls: Module class object
            force (bool, optional): Whether to override an existing class with
                the same name. Default: False.

        """
        if not (module_name is None or isinstance(module_name, str)):
            raise TypeError(f'module_name must be either of None, str,'
                            f'got {type(module_name)}')
        if module_cls is not None:
            self._register_module(
                group_key=group_key,
                module_name=module_name,
                module_cls=module_cls,
                force=force)
            return module_cls

        # if module_cls is None, should return a decorator function
        def _register(module_cls):
            self._register_module(
                group_key=group_key,
                module_name=module_name,
                module_cls=module_cls,
                force=force)
            return module_cls

        return _register


class registers():  # pylint: disable=invalid-name, too-few-public-methods

    def __init__(self):
        raise RuntimeError("Registries is not intended to be instantiated")

    pipelines = Register('pipelines')
    models = Register('models')


def import_all_modules_for_register():
    """Import all modules for register.

    Args:
        config (_type_, optional): _description_. Defaults to None.
    """
    all_modules = ALL_PIPELINES + ALL_MODELS
    for base_dir, modules in all_modules:
        for name in modules:
            try:
                if base_dir != '':
                    full_name = base_dir + '.' + name
                else:
                    full_name = name
                importlib.import_module(full_name)
            except ImportError as e:
                print(e)


def build_from_cfg(cfg: ConfigDict,
                   register: Register,
                   group_key: str = DEFAULT_GROUP_NAME) -> object:
    """Build a module (pipeline or model) from config dict

    Args:
        cfg (ConfigDict): configuration
        register (Register): _description_
        group_key (str, optional): _description_. Defaults to DEFAULT_GROUP_NAME.

    Raises:
        TypeError: _description_
        TypeError: _description_
        KeyError: _description_
        type: _description_

    Returns:
        object: _description_
    """
    
    if not isinstance(cfg, dict):
        raise TypeError(f'cfg must be a dict, but got {type(cfg)}')
    if not isinstance(register, Register):
        raise TypeError('register must be an opentablizer.utils.Register object, '
                        f'but got {type(register)}')

    import_all_modules_for_register()

    if group_key is None:
        group_key = DEFAULT_GROUP_NAME
        
    # args = cfg.copy()
    assert TYPE in cfg
    obj_type = cfg.type
    ic(register)
    ic(obj_type)
    ic(group_key)

    if isinstance(obj_type, str):
        obj_cls = register.get(obj_type, group_key=group_key)
        if obj_cls is None:
            raise KeyError(f'{obj_type} is not in the {register.name}'
                           f' register group {group_key}')
    # TODO 
    # elif inspect.isclass(obj_type) or inspect.isfunction(obj_type):
    #     obj_cls = obj_type
    # else:
    #     raise TypeError(
    #         f'type must be a str or valid type, but got {type(obj_type)}')
    try:
        if hasattr(obj_cls, '_instantiate'):
            return obj_cls._instantiate(cfg)
        else:
            return obj_cls(cfg)
    except Exception as e:
        # Normal TypeError does not print class name.
        raise type(e)(f'{obj_cls.__name__}: {e}')

