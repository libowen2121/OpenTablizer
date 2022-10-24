from abc import abstractmethod
from ast import Str
from turtle import forward
from addict import Dict
from typing import Union
from opentablizer.models.base import Model
from opentablizer.preprocessor.base import Preprocessor
from opentablizer.utils.config import ConfigDict


class Pipeline():
    """Base class for pipeline
    """
    
    def __init__(self, model: Model = None,
                 cfg: ConfigDict = None,) -> None:
                #  preprocessor: Union[Preprocessor, List[Preprocessor]] = None,
        """_summary_

        Args:
            cfg (ConfigDict, optional): _description_. Defaults to None.
        """        
        self.cfg = cfg
        self.model = model
        
    def __call__(self, 
                 input: Union[dict, Dict],
                 *args,
                 **extra_kwargs) -> Dict:
        return self.forward(input=input)
    
    def forward(self, input: Union[dict, Dict] = None, 
                **forward_params):
        from icecream import ic
        if isinstance(input, dict):
            input = Dict(**input)
        output = self.model(input, **forward_params)
        output = Dict(output=output)
        # output.update(input)
        return output
    
    def initiate_single_model(self, model):
        pass
    
    def initiate_multiple_models(self, models):
        pass
    
    def prepare_model(self):
        pass
    
    def preprocess(self, input: Union[dict, Dict]):
        pass

    def postprocess(self, output: Dict) -> Dict:
        pass