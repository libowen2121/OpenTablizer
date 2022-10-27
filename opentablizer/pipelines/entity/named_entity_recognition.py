from typing import Union
from addict import Dict
from opentablizer.models.base import Model
from opentablizer.pipelines.base import Pipeline
from opentablizer.utils.config import ConfigDict
from opentablizer.utils.constants import Pipelines, Tasks
from opentablizer.utils.register import registers


@registers.pipelines.register_module(
    Tasks.named_entity_recognition,
    module_name=Pipelines.named_entity_recognition
)
class NamedEntityRecognitionPipeline(Pipeline):
    
    def __init__(self, cfg: ConfigDict = None) -> None:
        cfg.type = cfg.model    # change the type to model
        if cfg.model_source == 'from_off_the_shelf':
            model = Model.from_off_the_shelf(cfg)
        elif cfg.model_source == 'from_rules':
            model = Model.from_rules(cfg)
        else:
            # TODO
            pass
        super().__init__(model, cfg)   # model has been instantiated
        # TODO

    def forward(self, input: Union[dict, Dict]) -> Dict:
        return super().forward(input)
    
    
