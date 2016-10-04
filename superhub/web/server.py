from functools import lru_cache
from time import gmtime, strftime

from flask import Flask, render_template
from flask import url_for
from werkzeug.utils import redirect

from superhub.pages import DeviceConnectionStatusPage, DhcpReservationPage, IpFilteringPage, MacFilteringPage, PortBlockingPage, PortForwardingPage, PortTriggeringPage
from superhub.router import Router
from superhub.utils.password_vault import PasswordVault

app = Flask(__name__)


@lru_cache()
def get_router():
    host = "192.168.0.1"
    password = PasswordVault().get()
    router = Router(host, password)
    router.login()
    print("Connected to router!")
    return router


def get_timestamp():
    return strftime("%Y-%m-%d %H:%M:%S %Z", gmtime())


@app.route("/")
def status():
    return redirect(url_for('devices'))


@app.route("/devices")
def devices():
    page = DeviceConnectionStatusPage(get_router())
    tables = [page.wired_devices, page.wireless_devices]
    return render_template("status.html", tables=tables, timestamp=get_timestamp(), active="devices")


@app.route("/dhcp")
def dhcp():
    page = DhcpReservationPage(get_router())
    tables = [page.ip_lease_table]
    return render_template("status.html", tables=tables, timestamp=get_timestamp(), active="dhcp")


@app.route("/ip")
def ip():
    page = IpFilteringPage(get_router())
    tables = [page.ip_filter_list]
    return render_template("status.html", tables=tables, timestamp=get_timestamp(), active="ip")


@app.route("/mac")
def mac():
    page = MacFilteringPage(get_router())
    tables = [page.mac_filter_list]
    return render_template("status.html", tables=tables, timestamp=get_timestamp(), active="mac")


@app.route("/ports")
def ports():
    tables = [
        PortBlockingPage(get_router()).port_blocking_rules,
        PortForwardingPage(get_router()).port_forwarding_rules,
        PortTriggeringPage(get_router()).port_triggering_rules,
    ]
    return render_template("status.html", tables=tables, timestamp=get_timestamp(), active="ports")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
