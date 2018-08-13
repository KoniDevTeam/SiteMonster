# SiteMonster
App that checks your website availability and sends notification to you if it is down.

**Platform**: **Windows/Linux** (**Debain/Ubuntu/Mint** *(deb packages, snap)*, **RHEL/CentOS/Fedora** *(rpm packages)*, **other linux** *(source compile)*)
## Download latest version
We will release the first version soon.
## Install from source on linux
Download latest source code from [here](https://github.com/KoniDevTeam/SiteMonster/releases).
Unzip source and run this in source folder:
```bash
make
make install
```
## Features
You can check your webites' availability directly in the app interface. Also, every second it is checking all your websites. If your website is down, app will report about it. The app can do the following:
* Send push notifications to your PC
* Play a loud alarm sound
## Planned features
* Translate the app to Russian and Ukrainian (v1.1)
* Port to macOS, add binaries for Arch linux (v1.1)
* Notifications for mobile phone (iOS, Android) (v1.1)
* Detailed configuration (v1.1)
* Email and telegram notifications (v1.2)
* sitemap.xml scanner (v1.2)
* Bad links search (v1.2)
## Contribution
You can freely contribute to our github. There're many things you can do: fix bugs, add new features, make translations. Please follow several simple rules:
* Create one pull request per one feature
* Create one commit for one small piece of implementation
* Write simple functions. Every function must do one small thing. All actions in function must be on one abstraction level.
* Specify type of return value and arguments, e.g.
```python 
def check(site: dict) -> bool:
    """Check if site is available."""
    
    pass
```
* Write pydocs if it's needed
* Write unit tests for your code (python unittest) and put it in "tests" folder
* Before starting pull request, run all unit tests to make sure that you did not break anything.
* Add your name to list of contributors in end of this file.
## License
![GNU GPL v3 logo](https://www.gnu.org/graphics/gplv3-127x51.png)

Site Monster is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Site Monster is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Site Monster.  If not, see <https://www.gnu.org/licenses/>.
## Authors and copyright
Copyright (C) 2018 Koni Dev Team, All Rights Reserved<br>
*For any questions contact <nikitaserba@icloud.com><br>*
**Project team:**
* Nikita Serba <<nikitaserba@icloud.com>>
* Mykola Bashmakov <<MrGraphitem@gmail.com>>

**Contributors:**
