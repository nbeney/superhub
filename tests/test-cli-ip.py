# import os
# import sys
#
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
#
# from click.testing import CliRunner
# from nose import with_setup
#
# from superhub.cli import cli
#
# runner = CliRunner()
#
#
# def run(args, expected=[], unexpected=[], fail=False):
#     prefix = ["--password", os.environ["SUPERHUB_PASSWORD"], "--keep-logged-in", "ip"]
#     res = runner.invoke(cli, prefix + args)
#     assert (not fail and res.exit_code == 0) or (fail and res.exit_code != 0)
#     for _ in expected:
#         assert _ in res.output, _
#     for _ in unexpected:
#         assert _ not in res.output, _
#
#
# def setup_func():
#     # run(["delete", "TEST*"])
#     pass
#
#
# def teardown_func():
#     # run(["delete", "TEST*"])
#     pass
#
#
# @with_setup(setup_func, teardown_func)
# def test_ip_list():
#     # run(["add", "TEST1", "11:11:11:11:11:11", "yes"])
#     # run(["list"], expected=["Device Name", "MAC Address", "Enable", "TEST1", "11:11:11:11:11:11", "True"])
#     run(["list"], expected=["Device Name", "MAC Address", "Enable", "DESKTOP-2PP2G25"])
