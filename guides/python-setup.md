# Python Setup
This is a simple guide to setup Python on your machine for this course.

Using VSCode can make using Python much easier as it supports automatically activating virtual environments.

## Download Python
Go to [python.org](https://python.org) and download the latest version for your machine.


## Virtual Environments

### Windows
In-depth guide [here](https://www.codingforentrepreneurs.com/guides/install-python-on-windows/)

```powershell
cd path\to\your\project
C:\Python310\python.exe -m venv venv
.\venv\Scripts\activate
```

Once activated you can run:

```powershell
python -m pip install pip --upgrade
```
or
```powershell
pip install pip --upgrade
```


### macOS

In-depth guide [here](https://www.codingforentrepreneurs.com/guides/install-python-on-macos/)


```bash
cd path/to/your/project
python3 -m venv venv
source venv/bin/activate
```

Once activated you can run:

```bash
python -m pip install pip --upgrade
```
or
```bash
pip install pip --upgrade
```