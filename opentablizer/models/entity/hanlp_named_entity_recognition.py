from addict import Dict
from opentablizer.models.base import Model
from opentablizer.utils.config import ConfigDict
from opentablizer.utils.constants import Models, Tasks
from opentablizer.utils.register import registers


@registers.models.register_module(
    Tasks.named_entity_recognition,
    module_name=Models.hanlp_named_entity_recognition)
class HanlpNamedEntityRecognition(Model):
    """Hanlp Named Entity Recognition
    """
    def __init__(self, cfg: ConfigDict = None) -> None:
        super().__init__(cfg)   # TODO
        import hanlp
        self.tokenizer = hanlp.load(hanlp.pretrained.tok.COARSE_ELECTRA_SMALL_ZH)
        self.ner = hanlp.load(hanlp.pretrained.ner.MSRA_NER_ELECTRA_SMALL_ZH)

    def forward(self, input: Dict):
        # from icecream import ic
        # ic(input.text)
        # ic(self.tokenizer(input.text))
        return self.ner(self.tokenizer(input.text))

    def postprocess(self, ner_result):
        return ner_result
    
