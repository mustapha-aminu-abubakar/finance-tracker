from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FloatField, DateTimeLocalField
from wtforms.validators import DataRequired
from wtforms.widgets import DateTimeInput

class IncomeForm(FlaskForm):
    amount = FloatField("Amount", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    date_ = DateTimeLocalField("Date", validators=[DataRequired()], render_kw={"type": "datetime-local"})
    source = StringField("Source", validators=[DataRequired()])
    submit = SubmitField("Add")
    
    
class ExpenseForm(FlaskForm):
    amount = FloatField("Amount", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    date_ = DateTimeLocalField("Date", validators=[DataRequired()], render_kw={"type": "datetime-local"})
    beneficiary = StringField("Beneficiary", validators=[DataRequired()])
    submit = SubmitField("Add")
   
   
class UpdateIncomeForm(FlaskForm):
    amount = FloatField("Amount")
    description = TextAreaField("Description")
    date_ = DateTimeLocalField("Date", render_kw={"type": "datetime-local"})
    source = StringField("Source")
    submit = SubmitField("Update")   


class UpdateExpenseForm(FlaskForm):
    amount = FloatField("Amount")
    description = TextAreaField("Description")
    date_ = DateTimeLocalField("Date", render_kw={"type": "datetime-local"})
    beneficiary = StringField("Beneficiary")
    submit = SubmitField("Update")   