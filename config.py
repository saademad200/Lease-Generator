import os
from enum import Enum

class FormType(Enum):
    DHA_LICENSE_A = "DHA License 'A'"
    # Add other form types here as needed
    # DHA_LICENSE_B = "DHA License 'B'"
    # TRANSFER_DEED = "Transfer Deed"
    # etc...

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here-change-in-production'
    UPLOAD_FOLDER = 'generated_docs'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Document Generation Settings
    DOCUMENT_TYPES = {
        FormType.DHA_LICENSE_A: {
            'title': "DHA License 'A'",
            'description': 'Defence Housing Authority Residential License Type A',
            'template': 'dha_license_a.docx'
        }
        # Add other document types here
    }
    
    # Form Field Defaults
    DEFAULT_VALUES = {
        FormType.DHA_LICENSE_A: {
            'licensee_name': 'Muhammad Ahmed',
            'licensee_address': 'House No. 123, Street 45\nPhase 6, DHA\nKarachi, Pakistan',
            'plot_area': '500',
            'plot_number': 'A-123',
            'survey_sheet_number': 'SS-456',
            'north_boundary': 'Plot A-124',
            'south_boundary': 'Road 5',
            'east_boundary': 'Plot A-122',
            'west_boundary': '30ft Road',
            'police_station': 'Defence Police Station',
            'territorial_division': 'South District',
            'land_size': '0.25',
            'deh': 'Defence Phase 6',
            'sub_registrar': 'DHA Sub-Registrar Office',
            'kpt_book_no': 'KPT-2024-001',
            'kpt_mf_roll_no': 'MF-2024-001',
            'premium_rate': 5000.00,
            'ground_rent_rate': 50.00,
            'transfer_order_no': 'TO-2024-001',
            'witness1_name': 'Muhammad Ali',
            'witness1_address': '456 DHA Phase 2\nKarachi, Pakistan',
            'witness1_cnic': '42201-1234567-8',
            'witness2_name': 'Ahmed Khan',
            'witness2_address': '789 DHA Phase 3\nKarachi, Pakistan',
            'witness2_cnic': '42201-8765432-1'
        }
    }

    @staticmethod
    def init_app(app):
        # Create upload folder if it doesn't exist
        if not os.path.exists(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER) 