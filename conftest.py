import pytest
from appium import webdriver
import time
import requests
from TG_bot.bot import send_telegram
import allure
from allure_commons.types import AttachmentType
import os

def pytest_addoption(parser):  # parser for device for tests
    parser.addoption('--device', action='store', default='SamsungPhone', help='Choose device: SamsungPhone, Emulator')
    parser.addoption('--p', action='store', default='4723', help='Choose appium port (4723 default)')  # for appium port

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):  # fixture that sets results of tests
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function")
def driver_mobile(request):
    # browser = None
    device = request.config.getoption('device')  # determining a device to past it into messages
    start_test_message = 'Test has been started: ' + request.node.name + '\n' + 'Device: ' + device
    print(start_test_message)   # logging
    send_telegram(start_test_message)
    app_path = str(os.getcwd()) + '/app.tjournal.apk'  # to make a path to the app independent from os
    device = request.config.getoption('device')
    if device == 'SamsungPhone':
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '11',  # android Samsung Galaxy A32
            'deviceName': 'SamsungGalaxyA32',  # android Samsung Galaxy A32
            'app': app_path,
            'autoGrantPermissions': 'true',
            'newCommandTimeout': '300',
        }
    elif device == 'Emulator':
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '11',  # android Samsung Galaxy A32
            'deviceName': 'Pixel_3_XL_API_30',  # emulator
            'app': app_path,
            'autoGrantPermissions': 'true',
            'newCommandTimeout': '300',

        }
    else:
        raise pytest.UsageError('--device should be named correctly: SansungPhone, Emulator')

    print("\nopen app..")
    print('Test starts: ', time.ctime())   # logging

    appium_port = request.config.getoption('p')  # appium port for parallel performance
    url_remote = 'http://127.0.0.1:' + str(appium_port) + '/wd/hub'  # appium port for parallel performance
    print(url_remote)
    driver = webdriver.Remote(url_remote, desired_caps)

    yield driver
    if request.node.rep_call.failed:
        fail_text = 'TEST FAILED'
        send_telegram(fail_text)
        report = request.node.rep_call.longreprtext
        if 'AssertionError' in report:    # from report - necessary part
            report_1 = report[report.find("driver"):report.rfind("_ _ _ _ _ _")]  # from 'driver' to '_ _ _' - to track an error
            report_2 = report[report.find("AssertionError"):]  # from 'AssertionError' to the end
            report = report_1 + '\n' + report_2
        elif 'AssertionError' not in report:
            report_1 = report[report.find("driver"):report.rfind("_ _ _ _ _ _")]  # from 'driver' to '_ _ _' - to track an error
            report_2 = report[report.rfind("E "):]  # from 'E  ' to the end
            report = report_1 + '\n' + report_2
        test_info_log = 'Test has been performed: ' + request.node.name + '\n' + '\n' + 'Result: ' + request.node.rep_call.outcome + '\n' + '\n' + 'Device: ' + device + '\n' + '\n' + 'Error report: ' + ' \n' + report
        test_info_telegram = 'Test has been performed: ' + request.node.name + '\n' + '\n' + 'Result: ' + request.node.rep_call.outcome + '\n' + '\n' + 'Device: ' + device + '\n' + '\n' + 'Error report: ' + ' \n' + report
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=request.function.__name__ + '_ERROR',
                attachment_type=AttachmentType.PNG
            )
        except:
            pass
    else:
        test_info_log = 'Test has been performed: ' + request.node.name + '\n' + '\n' + 'Result: ' + request.node.rep_call.outcome + '\n' + '\n' + 'Device: ' + device
        test_info_telegram = test_info_log
    print(test_info_log)
    for x in range(0, len(test_info_telegram), 4096):  # dividing into 4096 len messages: take 0, mess = [0;4096], send -> take  4096 (step) => 4096, mess = [4097;8193], send
        final_test_message_telegram = test_info_telegram[x: x + 4096]
        send_telegram(final_test_message_telegram)
    print("\nclose app..")
    driver.quit()

def pytest_sessionfinish(session):  # final message after session - results
    reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    print('\n')
    passed = 0
    failed = 0
    xfailed = 0
    skipped = 0
    xpassed = 0
    # in list => using if
    if 'passed' in reporter.stats:
        passed = len(reporter.stats['passed'])
    if 'failed' in reporter.stats:
        failed = len(reporter.stats['failed'])
    if 'xfailed' in reporter.stats:
        xfailed = len(reporter.stats['xfailed'])
    if 'skipped' in reporter.stats:
        skipped = len(reporter.stats['skipped'])
    if 'xpassed' in reporter.stats:
        xpassed = len(reporter.stats['xpassed'])

    duration = time.strftime("%H:%M:%S", time.gmtime(time.time() - reporter._sessionstarttime))
    total_not_counting_skip_xfail = round(((passed + skipped + xfailed) * 100) / (passed + failed + xfailed + skipped + xpassed), 2)
    total_counting_skip_xfail = round((passed*100)/(passed + failed + xfailed + skipped + xpassed), 2)
    result_message = 'passed amount: ' + str(passed) + '\n' + 'failed amount: ' + str(failed) + '\n' + 'xfailed amount: ' + str(xfailed) + '\n' + 'skipped amount: ' + str(skipped) + '\n' + 'xpassed amount: ' + str(xpassed) + '\n' + 'Total (skipped and xfailed = passed) ' + str(total_not_counting_skip_xfail) + '% \n' + 'Total (skipped and xfailed = failed) ' + str(total_counting_skip_xfail) + '% \n' + 'Duration: ' + str(duration) + ' sec'
    print(result_message)
    send_telegram(result_message)
