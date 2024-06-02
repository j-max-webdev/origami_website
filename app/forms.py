from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import sqlalchemy as sa
from app import db
from app.models import Designer

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class DesignerForm(FlaskForm):
    first_name = StringField("FirstName", validators=[DataRequired()])
    last_name = StringField("LastName", validators=[DataRequired()])
    adddesigner = SubmitField("Add Designer")

    def validate_last_name(self, last_name):
        designer_lname = db.session.scalar(sa.select(Designer).where(
            Designer.last_name == last_name.data)
        )

        print(designer_lname)

        if designer_lname is not None:
            raise ValidationError("The last name of this designer is already in the system")
