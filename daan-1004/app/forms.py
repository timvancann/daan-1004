from flask.ext.wtf import Form
import re
from wtforms import StringField, IntegerField, TextField, TextAreaField, FileField, HiddenField
from wtforms.validators import DataRequired, regexp
from wtforms_components import validators


class PaintingCreateForm(Form):
	title = StringField('Titel', validators=[DataRequired()])
	image = FileField('Schilderij', validators=[regexp('^[^/\\\\]\.jpg$')])
	notes = TextAreaField('Beschrijving')

	def validate_image(form, field):
		if field.data:
			field.data = re.sub('[^a-z0-9_.-]', '_', field.data)


class PaintingEditForm(Form):
	title = StringField('Titel', validators=[DataRequired()])
	notes = TextAreaField('Beschrijving')
	key = HiddenField('key')