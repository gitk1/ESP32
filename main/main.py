from ota_updater import OTAUpdater
import machine, time

def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/gitk1/ESP32.git')
    ota_updater.download_and_install_update_if_available('kritsnam', 'hydro123')

def start():
    led = machine.Pin(5, machine.Pin.OUT)
    i=0
    while (i<4):
        print("running")
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)
        i+=1

def boot():
    download_and_install_update_if_available()
    start()

boot()
