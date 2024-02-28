from flask import Blueprint
from api.v1.views import *
from api.vi.views.index import *
from api.vi.views.amenities import *
from api.vi.views.cities import *
from api.vi.views.users import *
from api.vi.views.places import *
from api.vi.views.reviews import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
