from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from datetime import datetime
from config import FormType, Config

class FormSelector(FlaskForm):
    form_type = SelectField('Select Document Type', 
                          choices=[(form_type.name, form_type.value) for form_type in FormType],
                          validators=[DataRequired()])

class DHALicenseForm(FlaskForm):
    # Licensee (2nd Party) Information
    licensee_name = StringField('Licensee Name (2nd Party)', 
                              validators=[DataRequired()],
                              default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['licensee_name'])
    licensee_address = TextAreaField('Licensee Address',
                                   validators=[DataRequired()],
                                   default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['licensee_address'])
    
    # Plot Details
    plot_area = StringField('Plot Area (Square Yards)',
                          validators=[DataRequired()],
                          default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['plot_area'])
    plot_number = StringField('Plot Number',
                           validators=[DataRequired()],
                           default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['plot_number'])
    survey_sheet_number = StringField('Survey Sheet Number',
                                   validators=[DataRequired()],
                                   default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['survey_sheet_number'])
    
    # Plot Boundaries
    north_boundary = StringField('North Boundary',
                              validators=[DataRequired()],
                              default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['north_boundary'])
    south_boundary = StringField('South Boundary',
                              validators=[DataRequired()],
                              default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['south_boundary'])
    east_boundary = StringField('East Boundary',
                             validators=[DataRequired()],
                             default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['east_boundary'])
    west_boundary = StringField('West Boundary',
                             validators=[DataRequired()],
                             default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['west_boundary'])
    
    # Police Station
    police_station = StringField('Police Station',
                              validators=[DataRequired()],
                              default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['police_station'])
    
    # Territorial Division
    territorial_division = StringField('Territorial Division',
                                    validators=[DataRequired()],
                                    default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['territorial_division'])
    
    # Land Details
    land_size = StringField('Land Size (Acres)',
                         validators=[DataRequired()],
                         default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['land_size'])
    deh = StringField('Deh',
                    validators=[DataRequired()],
                    default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['deh'])
    
    # KPT Details
    sub_registrar = StringField('Sub-Registrar Office',
                             validators=[DataRequired()],
                             default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['sub_registrar'])
    kpt_book_no = StringField('KPT Book Number',
                            validators=[DataRequired()],
                            default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['kpt_book_no'])
    kpt_book_date = DateField('KPT Book Date',
                           validators=[DataRequired()],
                           default=datetime.now())
    kpt_mf_roll_no = StringField('KPT MF Roll Number',
                               validators=[DataRequired()],
                               default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['kpt_mf_roll_no'])
    kpt_mf_roll_date = DateField('KPT MF Roll Date',
                              validators=[DataRequired()],
                              default=datetime.now())
    
    # Payment Details
    premium_rate = DecimalField('Premium Rate (Rs. per square yard)',
                             validators=[DataRequired()],
                             default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['premium_rate'])
    ground_rent_rate = DecimalField('Ground Rent Rate (paisas per square yard per annum)',
                                 validators=[DataRequired()],
                                 default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['ground_rent_rate'])
    
    # Transfer/Allotment Details
    transfer_order_no = StringField('Transfer/Allotment Order Number',
                                 validators=[DataRequired()],
                                 default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['transfer_order_no'])
    transfer_order_date = DateField('Transfer/Allotment Order Date',
                                 validators=[DataRequired()],
                                 default=datetime.now())
    
    # Witness Details
    witness1_name = StringField('Witness 1 Name',
                             validators=[DataRequired()],
                             default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['witness1_name'])
    witness1_address = TextAreaField('Witness 1 Address',
                                  validators=[DataRequired()],
                                  default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['witness1_address'])
    witness1_cnic = StringField('Witness 1 CNIC',
                             validators=[DataRequired()],
                             default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['witness1_cnic'])
    
    witness2_name = StringField('Witness 2 Name',
                             validators=[DataRequired()],
                             default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['witness2_name'])
    witness2_address = TextAreaField('Witness 2 Address',
                                  validators=[DataRequired()],
                                  default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['witness2_address'])
    witness2_cnic = StringField('Witness 2 CNIC',
                             validators=[DataRequired()],
                             default=Config.DEFAULT_VALUES[FormType.DHA_LICENSE_A]['witness2_cnic'])

class FormFactory:
    _forms = {
        FormType.DHA_LICENSE_A: DHALicenseForm
    }
    
    @staticmethod
    def create_form(form_type: FormType) -> FlaskForm:
        form_class = FormFactory._forms.get(form_type)
        if not form_class:
            raise ValueError(f"No form class registered for form type: {form_type}")
        return form_class()
    
    @staticmethod
    def register_form(form_type: FormType, form_class: FlaskForm):
        FormFactory._forms[form_type] = form_class 