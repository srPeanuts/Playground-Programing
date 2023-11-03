EXPECTED_BAKE_TIME = 40
def bake_time_remaining(actual_minutes):
  return EXPECTED_BAKE_TIME - actual_minutes
  
def preparation_time_in_minutes(number_of_layers):
  return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
  preparation_time = number_of_layers * 2
  return preparation_time + elapsed_bake_time