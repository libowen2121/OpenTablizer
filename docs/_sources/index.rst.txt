.. Open Tablizer documentation master file, created by
   sphinx-quickstart on Tue Oct 11 17:07:15 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Open Tablizer's documentation
=========================================


Getting Started
---------------


..  code-block:: python

   from opentablizer.pipelines import pipeline
   from opentablizer.postprocessor import postprocess

   # Run the pipeline
   ner = pipeline(task='ner', model='xxx', config_file='xxx')
   result_json_obj = ner(text='xxx')
   
   # Postprocess the output
   table_obj = postprocess(result_json_obj)

.. toctree::
   :glob:
   :maxdepth: 3
   :caption: Package Reference

   modules/pipeline
   modules/trainer
   modules/model


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
