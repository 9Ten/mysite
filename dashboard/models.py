from django.db import models

# Create your models here.
# from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.validators import FileExtensionValidator

from django.contrib.auth import get_user_model


User = get_user_model()


def abstract_handle(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    filename_ext = filename.split('.')[1]
    filename = str(instance.user).split('@')[0]
    return 'abstract/{}.{}'.format(filename, filename_ext)

def payment_handle(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    filename_ext = filename.split('.')[1]
    filename = str(instance.user).split('@')[0]
    return 'picture/{}.{}'.format(filename, filename_ext)


class UserProfile(models.Model):
    DEGREE_CHOICES = (
        ('prof.', 'Prof.'),
        ('dr.', 'Dr.'),
        ('post-doc', 'Post-Doc'),
        ('graduate', 'Graduate'),
        ('undergraduate', 'Undergraduate'),
        ('other', 'Other')
    )
    COUNTRY_CHOICES = [
        ('AF', 'Afghanistan'),
        ('AX', 'Aland Islands'),
        ('AL', 'Albania'),
        ('DZ', 'Algeria'),
        ('AS', 'American Samoa'),
        ('AD', 'Andorra'),
        ('AO', 'Angola'),
        ('AI', 'Anguilla'),
        ('AQ', 'Antarctica'),
        ('AG', 'Antigua and Barbuda'),
        ('AR', 'Argentina'),
        ('AM', 'Armenia'),
        ('AW', 'Aruba'),
        ('AU', 'Australia'),
        ('AT', 'Austria'),
        ('AZ', 'Azerbaijan'),
        ('BS', 'Bahamas'),
        ('BH', 'Bahrain'),
        ('BD', 'Bangladesh'),
        ('BB', 'Barbados'),
        ('BY', 'Belarus'),
        ('BE', 'Belgium'),
        ('BZ', 'Belize'),
        ('BJ', 'Benin'),
        ('BM', 'Bermuda'),
        ('BT', 'Bhutan'),
        ('BO', 'Bolivia'),
        ('BQ', 'Bonaire, Saint Eustatius and Saba '),
        ('BA', 'Bosnia and Herzegovina'),
        ('BW', 'Botswana'),
        ('BV', 'Bouvet Island'),
        ('BR', 'Brazil'),
        ('IO', 'British Indian Ocean Territory'),
        ('VG', 'British Virgin Islands'),
        ('BN', 'Brunei'),
        ('BG', 'Bulgaria'),
        ('BF', 'Burkina Faso'),
        ('BI', 'Burundi'),
        ('KH', 'Cambodia'),
        ('CM', 'Cameroon'),
        ('CA', 'Canada'),
        ('CV', 'Cape Verde'),
        ('KY', 'Cayman Islands'),
        ('CF', 'Central African Republic'),
        ('TD', 'Chad'),
        ('CL', 'Chile'),
        ('CN', 'China'),
        ('CX', 'Christmas Island'),
        ('CC', 'Cocos Islands'),
        ('CO', 'Colombia'),
        ('KM', 'Comoros'),
        ('CK', 'Cook Islands'),
        ('CR', 'Costa Rica'),
        ('HR', 'Croatia'),
        ('CU', 'Cuba'),
        ('CW', 'Curacao'),
        ('CY', 'Cyprus'),
        ('CZ', 'Czech Republic'),
        ('CD', 'Democratic Republic of the Congo'),
        ('DK', 'Denmark'),
        ('DJ', 'Djibouti'),
        ('DM', 'Dominica'),
        ('DO', 'Dominican Republic'),
        ('TL', 'East Timor'),
        ('EC', 'Ecuador'),
        ('EG', 'Egypt'),
        ('SV', 'El Salvador'),
        ('GQ', 'Equatorial Guinea'),
        ('ER', 'Eritrea'),
        ('EE', 'Estonia'),
        ('ET', 'Ethiopia'),
        ('FK', 'Falkland Islands'),
        ('FO', 'Faroe Islands'),
        ('FJ', 'Fiji'),
        ('FI', 'Finland'),
        ('FR', 'France'),
        ('GF', 'French Guiana'),
        ('PF', 'French Polynesia'),
        ('TF', 'French Southern Territories'),
        ('GA', 'Gabon'),
        ('GM', 'Gambia'),
        ('GE', 'Georgia'),
        ('DE', 'Germany'),
        ('GH', 'Ghana'),
        ('GI', 'Gibraltar'),
        ('GR', 'Greece'),
        ('GL', 'Greenland'),
        ('GD', 'Grenada'),
        ('GP', 'Guadeloupe'),
        ('GU', 'Guam'),
        ('GT', 'Guatemala'),
        ('GG', 'Guernsey'),
        ('GN', 'Guinea'),
        ('GW', 'Guinea-Bissau'),
        ('GY', 'Guyana'),
        ('HT', 'Haiti'),
        ('HM', 'Heard Island and McDonald Islands'),
        ('HN', 'Honduras'),
        ('HK', 'Hong Kong'),
        ('HU', 'Hungary'),
        ('IS', 'Iceland'),
        ('IN', 'India'),
        ('ID', 'Indonesia'),
        ('IR', 'Iran'),
        ('IQ', 'Iraq'),
        ('IE', 'Ireland'),
        ('IM', 'Isle of Man'),
        ('IL', 'Israel'),
        ('IT', 'Italy'),
        ('CI', 'Ivory Coast'),
        ('JM', 'Jamaica'),
        ('JP', 'Japan'),
        ('JE', 'Jersey'),
        ('JO', 'Jordan'),
        ('KZ', 'Kazakhstan'),
        ('KE', 'Kenya'),
        ('KI', 'Kiribati'),
        ('XK', 'Kosovo'),
        ('KW', 'Kuwait'),
        ('KG', 'Kyrgyzstan'),
        ('LA', 'Laos'),
        ('LV', 'Latvia'),
        ('LB', 'Lebanon'),
        ('LS', 'Lesotho'),
        ('LR', 'Liberia'),
        ('LY', 'Libya'),
        ('LI', 'Liechtenstein'),
        ('LT', 'Lithuania'),
        ('LU', 'Luxembourg'),
        ('MO', 'Macao'),
        ('MK', 'Macedonia'),
        ('MG', 'Madagascar'),
        ('MW', 'Malawi'),
        ('MY', 'Malaysia'),
        ('MV', 'Maldives'),
        ('ML', 'Mali'),
        ('MT', 'Malta'),
        ('MH', 'Marshall Islands'),
        ('MQ', 'Martinique'),
        ('MR', 'Mauritania'),
        ('MU', 'Mauritius'),
        ('YT', 'Mayotte'),
        ('MX', 'Mexico'),
        ('FM', 'Micronesia'),
        ('MD', 'Moldova'),
        ('MC', 'Monaco'),
        ('MN', 'Mongolia'),
        ('ME', 'Montenegro'),
        ('MS', 'Montserrat'),
        ('MA', 'Morocco'),
        ('MZ', 'Mozambique'),
        ('MM', 'Myanmar'),
        ('NA', 'Namibia'),
        ('NR', 'Nauru'),
        ('NP', 'Nepal'),
        ('NL', 'Netherlands'),
        ('NC', 'New Caledonia'),
        ('NZ', 'New Zealand'),
        ('NI', 'Nicaragua'),
        ('NE', 'Niger'),
        ('NG', 'Nigeria'),
        ('NU', 'Niue'),
        ('NF', 'Norfolk Island'),
        ('KP', 'North Korea'),
        ('MP', 'Northern Mariana Islands'),
        ('NO', 'Norway'),
        ('OM', 'Oman'),
        ('PK', 'Pakistan'),
        ('PW', 'Palau'),
        ('PS', 'Palestinian Territory'),
        ('PA', 'Panama'),
        ('PG', 'Papua New Guinea'),
        ('PY', 'Paraguay'),
        ('PE', 'Peru'),
        ('PH', 'Philippines'),
        ('PN', 'Pitcairn'),
        ('PL', 'Poland'),
        ('PT', 'Portugal'),
        ('PR', 'Puerto Rico'),
        ('QA', 'Qatar'),
        ('CG', 'Republic of the Congo'),
        ('RE', 'Reunion'),
        ('RO', 'Romania'),
        ('RU', 'Russia'),
        ('RW', 'Rwanda'),
        ('BL', 'Saint Barthelemy'),
        ('SH', 'Saint Helena'),
        ('KN', 'Saint Kitts and Nevis'),
        ('LC', 'Saint Lucia'),
        ('MF', 'Saint Martin'),
        ('PM', 'Saint Pierre and Miquelon'),
        ('VC', 'Saint Vincent and the Grenadines'),
        ('WS', 'Samoa'),
        ('SM', 'San Marino'),
        ('ST', 'Sao Tome and Principe'),
        ('SA', 'Saudi Arabia'),
        ('SN', 'Senegal'),
        ('RS', 'Serbia'),
        ('SC', 'Seychelles'),
        ('SL', 'Sierra Leone'),
        ('SG', 'Singapore'),
        ('SX', 'Sint Maarten'),
        ('SK', 'Slovakia'),
        ('SI', 'Slovenia'),
        ('SB', 'Solomon Islands'),
        ('SO', 'Somalia'),
        ('ZA', 'South Africa'),
        ('GS', 'South Georgia and the South Sandwich Islands'),
        ('KR', 'South Korea'),
        ('SS', 'South Sudan'),
        ('ES', 'Spain'),
        ('LK', 'Sri Lanka'),
        ('SD', 'Sudan'),
        ('SR', 'Suriname'),
        ('SJ', 'Svalbard and Jan Mayen'),
        ('SZ', 'Swaziland'),
        ('SE', 'Sweden'),
        ('CH', 'Switzerland'),
        ('SY', 'Syria'),
        ('TW', 'Taiwan'),
        ('TJ', 'Tajikistan'),
        ('TZ', 'Tanzania'),
        ('TH', 'Thailand'),
        ('TG', 'Togo'),
        ('TK', 'Tokelau'),
        ('TO', 'Tonga'),
        ('TT', 'Trinidad and Tobago'),
        ('TN', 'Tunisia'),
        ('TR', 'Turkey'),
        ('TM', 'Turkmenistan'),
        ('TC', 'Turks and Caicos Islands'),
        ('TV', 'Tuvalu'),
        ('VI', 'U.S. Virgin Islands'),
        ('UG', 'Uganda'),
        ('UA', 'Ukraine'),
        ('AE', 'United Arab Emirates'),
        ('GB', 'United Kingdom'),
        ('US', 'United States'),
        ('UM', 'United States Minor Outlying Islands'),
        ('UY', 'Uruguay'),
        ('UZ', 'Uzbekistan'),
        ('VU', 'Vanuatu'),
        ('VA', 'Vatican'),
        ('VE', 'Venezuela'),
        ('VN', 'Vietnam'),
        ('WF', 'Wallis and Futuna'),
        ('EH', 'Western Sahara'),
        ('YE', 'Yemen'),
        ('ZM', 'Zambia'),
        ('ZW', 'Zimbabwe')
    ]
    TITLE_CHOICES = [
        ('mr.', 'Mr.'),
        ('miss', 'Miss'),
        ('mrs.', 'Mrs.'),
        ('ms.', 'Ms.'),
        ('dr.', 'Dr.'),
        ('prof', 'Professor'),
        ('other', 'Other')
    ]

    #=== Addition register_form ===#
    USER_TYPE_CHOICES = [
        ('delegate', 'Delegate'),
        ('student', 'Student')
    ]
    PRESENTATION_CHOICES = [
        ('oral', 'Oral presentation'),
        ('poster', 'Poster presentation'),
        ('oral_poster', 'Both oral and poster presentation'),
    ]
    SIZE_CHOICES = [
        ('s', 'S (Chest: 36 inch)'),
        ('m', 'M (Chest: 38 inch)'),
        ('l', 'L (Chest: 40 inch)'),
        ('xl', 'XL (Chest: 42 inch)'),
        ('xxl', 'XXL (Chest: 44 inch)'),
        ('xxxl', 'XXXL (Chest: 46 inch)'),
    ]
    DIETARY_CHOICES = [
        ('none', 'None'),
        ('halal', 'Halal'),
        ('vegan', 'Vegan'),
        ('other', 'Other'),
    ]

    USER_STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
    ]
    STATUS_CHOICES = [
        ('-', '-'),
        ('accepted', 'Accepted'),
    ]

    #=== Section userprofile ===#
    user = models.OneToOneField(User, on_delete=models.CASCADE)     # Email

    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mid_name = models.CharField(max_length=30)
    institution = models.CharField(max_length=30)
    unit = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30)
    degree = models.CharField(max_length=30, choices=DEGREE_CHOICES)
    country = models.CharField(max_length=30, choices=COUNTRY_CHOICES)
    institution_country = models.CharField(max_length=30, choices=COUNTRY_CHOICES)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    user_type = models.CharField(max_length=30, choices=USER_TYPE_CHOICES, default='delegate')
    user_status = models.CharField(max_length=30, choices=USER_STATUS_CHOICES, default='waiting')
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # accept = models.BooleanField(default=False)

    #=== Addition register_form ===#
    presentation_type = models.CharField(max_length=30, choices=PRESENTATION_CHOICES, default='oral')
    shirt_size = models.CharField(max_length=30, choices=SIZE_CHOICES, default='s')
    dietary_restriction = models.CharField(max_length=30, choices=DIETARY_CHOICES, default='none')
    dietary_other = models.CharField(max_length=50, blank=True)

    #=== Section dashboard ===#
    # abstract
    # description = models.CharField(max_length=255, blank=True)
    abstarct_file = models.FileField(upload_to=abstract_handle, validators=[FileExtensionValidator(['pdf', 'docx', 'rtf'])], help_text="Browse a file")
    abstarct_file_uploaded = models.DateTimeField(null=True, blank=True)
    abstarct_file_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='-')
    # payment-thai
    slip_pic = models.ImageField(upload_to=payment_handle, validators=[FileExtensionValidator(['jpg', 'png'])], help_text="Browse a picture")
    # payment-national
    paypal_trans_id = models.CharField(max_length=17)
    payment_uploaded = models.DateTimeField(null=True, blank=True)
    payment_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='-')

    REQUIRED_FIELDS = [
        'title',
        'first_name',
        'last_name',
        'institution',
        'department',
        'degree',
        'country',
        'phone_number',
        'user_type',

        'presentation_type',
        'shirt_size',
        'dietary_restriction',
    ]

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
