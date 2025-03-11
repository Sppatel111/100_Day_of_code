from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Email

# Initialize Flask app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Custom ModelView for User
class CustomUserView(ModelView):
    form_base_class = SecureForm  # Use a secure form

    # Customize the form fields
    form_extra_fields = {
        'username': StringField('Username', validators=[DataRequired()]),
        'email': EmailField('Email', validators=[DataRequired(), Email()]),
    }

    # Customize the list view
    column_labels = {
        'username': 'User Name',
        'email': 'Email Address',
    }

    # Customize the list view columns
    column_list = ('id', 'username', 'email')

    # Customize the form layout
    form_args = {
        'username': {
            'label': 'User Name',
            'validators': [DataRequired()],
        },
        'email': {
            'label': 'Email Address',
            'validators': [DataRequired(), Email()],
        },
    }

    # Override the method to customize the behavior after saving
    def on_model_change(self, form, model, is_created):
        # You can add custom logic here, e.g., logging or modifying data
        print(f'User {"created" if is_created else "updated"}: {model.username}')

# Initialize Flask-Admin
admin = Admin(app, name='My Admin', template_mode='bootstrap3')
admin.add_view(CustomUserView(User, db.session))

# Create the database and tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
