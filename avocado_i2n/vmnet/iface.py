"""

SUMMARY
------------------------------------------------------
Interface object for the vmnet utility.

Copyright: Intra2net AG


CONTENTS
------------------------------------------------------
This is the basic building block of the vm network. Interfaces are grouped
in vmnodes (the virtual machines they belong to) and in netconfigs (the
local networks they define together).


INTERFACE
------------------------------------------------------

"""


class Interface(object):
    """The interface class."""

    """Structural vmnet properties"""
    def vmnode(self, value=None):
        """A reference to the vmnode the interface belongs to."""
        if value is not None:
            self._vmnode = value
        else:
            return self._vmnode
    vmnode = property(fget=vmnode, fset=vmnode)

    def netconfig(self, value=None):
        """A reference to the netconfig the interface belongs to."""
        if value is not None:
            self._netconfig = value
        else:
            return self._netconfig
    netconfig = property(fget=netconfig, fset=netconfig)

    def params(self, value=None):
        """The interface filtered test parameters."""
        if value is not None:
            self._params = value
        else:
            return self._params
    params = property(fget=params, fset=params)

    """Configuration properties"""
    def mac(self, value=None):
        """MAC address used by the network interface."""
        if value is not None:
            self._mac = value
        else:
            return self._mac
    mac = property(fget=mac, fset=mac)

    def ip(self, value=None):
        """IP address used by the network interface."""
        if value is not None:
            self._ip = value
        else:
            return self._ip
    ip = property(fget=ip, fset=ip)

    def __init__(self, params):
        """
        Construct an interface with configuration from the parameters.

        :param params: configuration parameters
        :type params: {str, str}
        """
        self._vmnode = None
        self._netconfig = None
        self._params = params

        self._mac = params["mac"]
        self._ip = params["ip"]

    def __repr__(self):
        vm_name = "none" if self.vmnode is None else self.vmnode.name
        net_name = "none" if self.netconfig is None else self.netconfig.net_ip
        iface_tuple = (self.ip, self.mac, vm_name, net_name)
        return "[iface] addr='%s', mac='%s' platform='%s' netconfig='%s'" % iface_tuple
