from django.core.exceptions import ValidationError

def validate_postal_code(value):
    if len(str(value)) != 10:
        raise ValidationError(
            'not a 10 digit postal code',
            params = {'value': value}
        )