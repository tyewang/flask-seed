import inspect
import vcr

from app import gateways, app

gateways_using_oauth = ['yelp_gateway']
def _vcr_record_gateways():
    for attribute_name in dir(gateways):
        if 'gateway' in attribute_name:
            gateway = getattr(gateways, attribute_name)
            _decorate_methods_in_gateway(gateway)

def _decorate_methods_in_gateway(gateway):
    for attribute_name in dir(gateway):
        attribute = getattr(gateway, attribute_name)
        is_public_function = inspect.isfunction(attribute) and not attribute_name.startswith('_')
        if is_public_function:
            match_on_url = gateway.__name__.split('.')[-1] in gateways_using_oauth
            setattr(gateway, attribute_name, _create_recorded_function(attribute, match_on_url))

def _create_recorded_function(f, match_on_url):
    def recorded_function(*args, **kwargs):
        match_on_options = match_on_url and {'match_on': ['method', 'scheme', 'host', 'port']} or {}
        with vcr.use_cassette('tests/cassettes/%s.yaml' % f.func_name, **match_on_options):
            return f(*args, **kwargs)

    return recorded_function

_vcr_record_gateways()
app.app_context().push()
