import sys
sys.path.append('../')
from icecream import ic

from opentablizer.pipelines.builder import pipeline

ner_pipeline = pipeline(task='named-entity-recognition',
                model='regex_named_entity_recognition',
                model_source='from_rules')
output = ner_pipeline({'text': '新华社北京二月十一日电（记者唐虹）', 'schema': ['日期'], 'pattern': ['[\d一二三四五六七八九十]+月[\d一二三四五六七八九十]+日']})
ic(output)
