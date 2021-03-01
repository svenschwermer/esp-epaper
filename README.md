# README
```sh
export ESPIDF=$(realpath esp-idf)
(cd $ESPIDF && ./install.sh)

python3 -m venv venv
. ./source-me
pip install -r $ESPIDF/requirements.txt

make -C micropython/mpy-cross
make -C micropython/ports/esp32 submodules
make -C micropython/ports/esp32 BOARD=GENERIC_SPIRAM

make -C micropython/ports/esp32 BOARD=GENERIC_SPIRAM PORT=/dev/tty.SLAB_USBtoUART erase
make -C micropython/ports/esp32 BOARD=GENERIC_SPIRAM PORT=/dev/tty.SLAB_USBtoUART deploy
```
