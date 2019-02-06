"""

SUMMARY
------------------------------------------------------
Run the steps necessary to make sure a vm has internet access.

Copyright: Intra2net AG


CONTENTS
------------------------------------------------------
Compared to :py:mod:`testsuite.host.tests.shared_set_provider`,
this test ends in an online state.


INTERFACE
------------------------------------------------------

"""

import logging
import time
import os

# avocado imports
from avocado.core import exceptions

# custom imports
pass


###############################################################################
# TEST MAIN
###############################################################################

def run(test, params, env):
    """
    Main test run.

    :param test: test object
    :param params: extended dictionary of parameters
    :param env: environment object
    """
    vmnet = env.get_vmnet()
    vm, _ = vmnet.get_single_vm_with_session()

    vmnet.ping()
