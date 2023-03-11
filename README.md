# README
```sh
export ESPIDF=$(realpath esp-idf)
(cd $ESPIDF && ./install.sh)

python3 -m venv venv
. ./source-me
pip install -r $ESPIDF/requirements.txt

make -C micropython/mpy-cross
make -C micropython/ports/esp32 submodules
make -C micropython/ports/esp32 BOARD=GENERIC_SPIRAM PYTHON2=python3

make -C micropython/ports/esp32 BOARD=GENERIC_SPIRAM PORT=/dev/ttyUSB0 erase
make -C micropython/ports/esp32 BOARD=GENERIC_SPIRAM PORT=/dev/ttyUSB0 deploy
```

Get a REPL via serial, type `help()`, connect to WiFi, transfer all files from
src/ to device via [webrepl](https://github.com/micropython/webrepl). Create
files `wifi_ssid`, `wifi_key` and `key_secret`. Run
`import upip; upip.install('urequests')`.
