class Temperature():

  # Store temperature readings
  # TODO: Replace dummy data with sensor readings
  readings = {
  1:21.0,
  2:20.3,
  3:20.1,
  4:20.9
  }

  @classmethod
  async def all_readings(cls):
    """Get a list of all recorded temps"""
    return cls.readings

  @classmethod
  async def last_reading(cls):
    """Get a list of all recorded temps"""
    return cls.readings[max(cls.readings.keys())]

# TODO: define and implement rest of functions for Temperature object
