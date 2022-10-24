import addict


class ConfigDict(addict.Dict):
    """Default class for configuration

    Args:
        addict (_type_): _description_
        
    Examples:
    >>> cdict = ConfigDict({'a':1232})
    >>> print(cdict.a)
    1232
    """    

    def __missing__(self, name):
        raise KeyError(name)

    def __getattr__(self, name):
        try:
            value = super(ConfigDict, self).__getattr__(name)
        except KeyError:
            ex = AttributeError(f"'{self.__class__.__name__}' object has no "
                                f"attribute '{name}'")
        except Exception as e:
            ex = e
        else:
            return value
        raise ex


# clean up test code
if __name__ == '__main__':
    cfg = ConfigDict(model='transformer')
    cfg.device = 'gpu' 
    
    from icecream import ic
    ic(cfg)