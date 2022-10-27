from addict import Dict
from opentablizer.models.base import Model
from opentablizer.utils.config import ConfigDict
from opentablizer.utils.constants import Models, Tasks
from opentablizer.utils.register import registers

import re


@registers.models.register_module(
    Tasks.named_entity_recognition,
    module_name=Models.regex_named_entity_recognition)
class RegexNamedEntityRecognition(Model):
    """Named Entity Recognition by regualr expression
    """
    def __init__(self, cfg: ConfigDict = None) -> None:
        super().__init__(cfg)   # TODO

    def forward(self, input: Dict):
        output = Dict()
        for s, p in zip(input.schema, input.pattern):
           output[s] = [] 
           for match in re.finditer(p, input.text):
                output[s].append((match.group(), match.span()))
        return output

    def postprocess(self, ner_result):
        return ner_result
    
