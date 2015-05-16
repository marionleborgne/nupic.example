from model_params.template_model_params import MODEL_PARAMS as TEMPLATE_MODEL_PARAMS
import csv
import os


class IncorrectHeadersException(Exception):
  pass

def create_model_params(model_param_dir, model_param_name, file_name):
  
  # get the scalar values
  values = []
  with open(file_name, 'rU') as inputFile:
    csvReader = csv.reader(inputFile)
    headers = csvReader.next()
    
    # skip the rest of the header rows
    csvReader.next()
    csvReader.next()
    
    if len(headers) != 2:
      raise IncorrectHeadersException("Number of columns in the CSV file should be 2 but is '%s'" %len(headers))
    if headers[0] != 'timestamp':
      raise IncorrectHeadersException("first column should be named 'timestamp' but is '%s'" %headers[0])
    if headers[1] != 'scalar_value':
      raise IncorrectHeadersException("first column should be named 'scalar_value' but is '%s'" %headers[1])
  
    for line in csvReader:
      values.append(float(line[1]))
      
  # make sure the directory exists
  if not os.path.exists(model_param_dir):
      os.makedirs(model_param_dir)
      
  # make sure there is an init file so that we can import the model_params file later 
  with open("%s/%s" % (model_param_dir, "__init__.py"), 'wb') as initFile:
    initFile.write("")
    
  # write the new model_params file
  with open("%s/%s.py" % (model_param_dir, model_param_name), 'wb') as modelParamsFile:
    min_value = min(values)
    max_value = max(values)
    mp = TEMPLATE_MODEL_PARAMS
    mp['modelParams']['sensorParams']['encoders']['_classifierInput']['maxval'] = max_value
    mp['modelParams']['sensorParams']['encoders']['_classifierInput']['minval'] = min_value
    mp['modelParams']['sensorParams']['encoders']['metric_value']['maxval'] = max_value
    mp['modelParams']['sensorParams']['encoders']['metric_value']['minval'] = min_value
    modelParamsFile.write("MODEL_PARAMS = %s" % repr(mp))



if __name__ == "__main__":
  
  FILE_NAME = 'scalar_data.csv'
  MODEL_PARAM_DIR = 'model_params'
  MODEL_PARAM_NAME = 'scalar_data_model_params'
  create_model_params(MODEL_PARAM_DIR, MODEL_PARAM_NAME, FILE_NAME)