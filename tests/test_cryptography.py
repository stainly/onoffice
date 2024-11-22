from onoffice.cryptography import create_hmac
from onoffice.resources import Resource
from onoffice.actions import Action


def test_create_hmac():
    hmac = create_hmac(
        token="ABC",
        secret="DEF",
        timestamp=1,
        resource=Resource.AGENTSLOG,
        action=Action.READ,
    )
    assert hmac == "LwCseeLgixJg7NtMk+9U1YiOSxVOpvsP7W60ASBzGgI="
