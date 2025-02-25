import sys
sys.path.append("../")

import pytest
import os
from payments import Pix

def test_pix_create_payment():
    pix_instance = Pix()

    #create a payment
    payment_info = pix_instance.create_payment(base_dir="../")

    assert "bank_payment_id" in payment_info