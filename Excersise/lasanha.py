EXPECTED_BAKE_TIME = 40

def bake_time_remaining(actual_minutes):
  return EXPECTED_BAKE_TIME - actual_minutes
  
def preparation_time_in_minutes(number_of_layers):
  return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
  preparation_time = number_of_layers * 2
  return preparation_time + elapsed_bake_time

print(bake_time_remaining(15)) #should print 25 (it takes 40 to bake and it has been baking for 15 min)

print(preparation_time_in_minutes(4)) #should print 8 because 4(layers) * 2 min per layer

print(elapsed_time_in_minutes(4,15)) #should print 23 (because 4 layers takes 8 min of prep plus the time that has been on the oven 15 min)