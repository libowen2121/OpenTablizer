from typing import Union, List
from opentablizer.model.base import Model
from opentablizer.preprocessor.base import Preprocessor


class Pipeline():
    """Base class for pipeline
    """
    
    def __init__(self,
                 config_file: str = None,
                 model: Union[Model, List[Model]] = None,
                 preprocessor: Union[Preprocessor, List[Preprocessor]] = None,
                 device: str = 'gpu',
                 **kwargs) -> None:
        """_summary_

        Args:
            config_file (str, optional): _description_. Defaults to None.
            model (Union[Preprocessor, List[Preprocessor]], optional): _description_. Defaults to None.
            preprocessor (Union[Preprocessor, List[Preprocessor]], optional): _description_. Defaults to None.
            device (str, optional): _description_. Defaults to 'gpu'.
        """        
        pass