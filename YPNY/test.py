import unittest
from lib.HwTestReport import HTMLTestReport


test_list=unittest.defaultTestLoader.discover(
    start_dir="TestCase",
    pattern="*.py"
)

file = open('report/report.html', 'wb')

runner = HTMLTestReport(
    stream=file,
    verbosity=2,
    images=True,
    title='HwTestReport 测试',
    tester='李诗涵'
)

runner.run(test_list)
file.close()