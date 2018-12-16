from aiohttp.web import Response, View, json_response
from aiohttp_cors import CorsViewMixin

from models.readings import Temperature, Pressure, Humidity, Gas, Light
from functools import wraps
import jwt


JWT_ALG = "HS256"

# decorator for methods with required authentication token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        request = args[0].request
        token = None

        try:
            auth = request.headers['authorization']
        except KeyError as keyErr:
            print(keyErr)
            return json_response({'message' : 'Missing token'}, status=401)

        try:
            token = auth#[7::]
            print(token)
            data = jwt.decode(token, request.app['JWT_KEY'], algorithms=JWT_ALG)
            print("DAT: ", data)
            current_user = data['login']
            print("User: ", current_user)
        except jwt.ExpiredSignatureError:
            return Response(text='Signature expired. Please log in again.')
        except jwt.InvalidTokenError:
            return Response(text='Invalid token. Please log in again.')

        return f(*args, current_user, **kwargs)

    return decorated


class TempsView(View, CorsViewMixin):
    """
    Temperature view
    """

    @token_required
    async def get(self, current_user):
      """ Return JSON with all temperature readings """
      login = None
      try:
        login = self.request.match_info.get('login')
      except Exception as e:
          print(e)
          print("Login needed")
        
      if login != current_user:
        return Response(text="You have no power here!", status=403)

      return json_response(await Temperature.all_readings(current_user), status=200)


class LastTempView(View, CorsViewMixin):
    """
    Last temperature view (most recent reading)
    """

    @token_required
    async def get(self, current_user):
      """ Return JSON with the current temperature reading """
      login = None
      try:
        login = self.request.match_info.get('login')
      except Exception as e:
          print(e)
          print("Login needed")
        
      if login != current_user:
        return Response(text="You have no power here!", status=403)

      return json_response(await Temperature.last_reading(current_user), status=200)


class PressView(View, CorsViewMixin):
    """
    Pressure view
    """

    @token_required
    async def get(self, current_user):
      """ Return JSON with all pressure readings """
      login = None
      try:
        login = self.request.match_info.get('login')
      except Exception as e:
          print(e)
          print("Login needed")
        
      if login != current_user:
        return Response(text="You have no power here!", status=403)
        
      return json_response(await Pressure.all_readings(current_user), status=200)

class LastPressView(View, CorsViewMixin):
    """
    Last pressure view (most recent reading)
    """

    @token_required
    async def get(self, current_user):
      """ Return JSON with the current pressure reading """
      login = None
      try:
        login = self.request.match_info.get('login')
      except Exception as e:
          print(e)
          print("Login needed")
        
      if login != current_user:
        return Response(text="You have no power here!", status=403)

      return json_response(await Pressure.last_reading(current_user), status=200)


class HumidView(View, CorsViewMixin):
    """
    Humidity view
    """
    
    @token_required
    async def get(self, current_user):
      """ Return JSON with all humidity readings """
      login = None
      try:
        login = self.request.match_info.get('login')
      except Exception as e:
          print(e)
          print("Login needed")
        
      if login != current_user:
        return Response(text="You have no power here!", status=403)

      return json_response(await Humidity.all_readings(current_user), status=200)

class LastHumidView(View, CorsViewMixin):
    """
    Last humidity view (most recent reading)
    """

    @token_required
    async def get(self, current_user):
      """ Return JSON with the current humidity reading """
      login = None
      try:
        login = self.request.match_info.get('login')
      except Exception as e:
          print(e)
          print("Login needed")
        
      if login != current_user:
        return Response(text="You have no power here!", status=403)

      return json_response(await Humidity.last_reading(current_user), status=200)


class GasView(View, CorsViewMixin):
    """
    Gas view
    """

    @token_required
    async def get(self, current_user):
      """ Return JSON with all gas readings """
      login = None
      try:
        login = self.request.match_info.get('login')
      except Exception as e:
          print(e)
          print("Login needed")
        
      if login != current_user:
        return Response(text="You have no power here!", status=403)

      return json_response(await Gas.all_readings(current_user), status=200)

class LastGasView(View, CorsViewMixin):
    """
    Last gas view (most recent reading)
    """

    @token_required
    async def get(self, current_user):
      """ Return JSON with the current gas reading """
      login = None
      try:
        login = self.request.match_info.get('login')
      except Exception as e:
          print(e)
          print("Login needed")
        
      if login != current_user:
        return Response(text="You have no power here!", status=403)

      return json_response(await Gas.last_reading(current_user), status=200)


class LightView(View, CorsViewMixin):
    """
    Light view
    """

    @token_required
    async def get(self, current_user):
      """ Return JSON with all light readings """
      login = None
      try:
        login = self.request.match_info.get('login')
      except Exception as e:
          print(e)
          print("Login needed")
        
      if login != current_user:
        return Response(text="You have no power here!", status=403)

      return json_response(await Light.all_readings(current_user), status=200)

class LastLightView(View, CorsViewMixin):
    """
    Last light view (most recent reading)
    """

    @token_required
    async def get(self, current_user):
      """ Return JSON with the current light reading """
      login = None
      try:
        login = self.request.match_info.get('login')
      except Exception as e:
          print(e)
          print("Login needed")
        
      if login != current_user:
        return Response(text="You have no power here!", status=403)
        
      return json_response(await Light.last_reading(current_user), status=200)