from flask import Blueprint

sample = Blueprint('sample', __name__, template_folder='templates')

@sample.route('/')
def sample_index():
	return "this is sample's index"