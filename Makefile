all:
	pyinstaller main/main.py
	mv dist/main/main dist/main/sitemonster
	mv dist/main/* dist/
	cp -R media/ dist/
	pyinstaller main/updater_main.py
	mv dist/updater_main/updater_main dist/updater
	rm -rf dist/updater_main/
	pyinstaller main/daemon_main.py
	mv dist/daemon_main/daemon_main dist/daemon
	rm -rf dist/daemon_main/
	LC_ALL=C find / -name "*audioop*.so" -print -quit 2>&1 | grep -v "Permission denied" | xargs cp -t dist/
	LC_ALL=C find / -name "*portaudio*.so" -print -quit 2>&1 | grep -v "Permission denied" | xargs cp -t dist/
	LC_ALL=C find ./ -name "*audioop*.so" -print -quit 2>&1 | grep -v "Permission denied" | xargs -I{} mv {} dist/audioop.so
	cp LICENSE dist/
prep:

	pip3 install pyaudio
	pip3 install requests
	pip3 install psutil
	sudo apt-get install -y python3-pyqt5 pyqt5-dev-tools
deb:
snap:
rpm:
install:
clean:
	rm -rf build dist *.spec
