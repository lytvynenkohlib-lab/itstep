import inspect
import requests
import math
import para3_sims

print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))
print(inspect.getmodule(math.sqrt))
print(inspect.getmodule(para3_sims.to_repair))
