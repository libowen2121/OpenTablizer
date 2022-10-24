import sys
sys.path.append('../../')

from abc import ABC, abstractmethod
from opentablizer.utils.config import ConfigDict

from opentablizer.utils.register import build_from_cfg, registers

class Model(ABC):
    """Base class for model
    """    

    def __init__(self, *args, **kwargs) -> None:
        pass

    def __call__(self, *args, **kwargs):
        return self.postprocess(self.forward(*args, **kwargs))
    
    @abstractmethod
    def forward(self, *args, **kwargs):
        pass

    def postprocess(self, *args, **kwargs):
        pass
    
    @classmethod
    def _instantiate(cls, *args, **kwargs):
        return cls(*args, **kwargs)
    
    @classmethod
    def from_pretrained(cls,
                        model_name_or_path: str,
                        cfg: ConfigDict = None,
                        device: str = None,
                        *model_args,
                        **kwargs):
        """ Instantiate a model from local directory or remote model repo.
        """
        pass
        model = build_from_cfg(cfg, registers.models, group_key=cfg.task)
    
    @classmethod
    def save_pretrained():
        pass
    
    @staticmethod
    def from_off_the_shelf(cfg: ConfigDict):
        return build_from_cfg(cfg, registers.models, group_key=cfg.task)
    
    @classmethod
    def from_rules():
        pass
    
if __name__ == '__main__':
    Model.from_off_the_shelf()