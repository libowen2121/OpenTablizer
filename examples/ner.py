import sys
sys.path.append('../')
from icecream import ic

from opentablizer.pipelines.builder import pipeline

ner_pipeline = pipeline(task='named-entity-recognition',
                model='hanlp_named_entity_recognition',
                model_source='from_off_the_shelf')
output = ner_pipeline({'text': '2021年测试高血压是138，时间是午饭后2点45，低血压是44'})
ic(output)
