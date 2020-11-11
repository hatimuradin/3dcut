from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (user.pk + timestamp + user.customer.signup_confirmation)

account_activation_token = AccountActivationTokenGenerator()
