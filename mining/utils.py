import uuid


def generate_referral_code():
    code = str(uuid.uuid4()).replace("-", "")[:7]
    return code