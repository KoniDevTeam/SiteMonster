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
	LC_ALL=C find / -name "*portaudio*cpython*.so" -print -quit 2>&1 | grep -v "Permission denied" | xargs cp -t dist/
	LC_ALL=C find ./ -name "*audioop*.so" -print -quit 2>&1 | grep -v "Permission denied" | xargs -I{} mv {} dist/audioop.so
	cp LICENSE dist/
prep:

	pip3 install pyaudio
	pip3 install requests
	pip3 install psutil
	sudo apt-get install -y python3-pyqt5 pyqt5-dev-tools
deb:
	mkdir -p deb-build/
	mkdir deb-build/DEBIAN
	mkdir -p deb-build/opt/SiteMonster
	cp -R dist/* deb-build/opt/SiteMonster/
	cp build-info/control deb-build/DEBIAN/
	cp build-info/copyright deb-build/DEBIAN/
	mkdir -p deb-build/etc/init.d
	chmod 644 deb-build/opt/SiteMonster/*.so
	mkdir -p deb-build/usr/share/applications
	cp build-info/Site\ Monster.desktop deb-build/usr/share/applications/
	cp build-info/daemon.desktop deb-build/usr/share/applications/
	fakeroot dpkg-deb --build deb-build/
	mv deb-build.deb sitemonster_1.0-1_all.deb
make rpm:
	sudo alien --to-rpm --scripts -g -v ./sitemonster_1.0-1_all.deb
	sudo rm -f sitemonster-1.0/sitemonster-1.0-2.spec
	sudo cp build-info/sitemonster-1.0-2.spec sitemonster-1.0/
	cd sitemonster-1.0; rpmbuild --buildroot='/media/files/Projects/Site Monster/sitemonster-1.0' -bb --target noarch 'sitemonster-1.0-2.spec' 2>&1
install:
	sudo mkdir "/opt/Site Monster/"
	sudo cp -r dist/* /opt/Site\ Monster/
	sudo cp build-info/*.desktop /usr/share/applications/
clean:
	sudo rm -rf build dist *.spec deb-build *.deb sitemonster-1.0 *.rpm
