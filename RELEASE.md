## Speedtest Tracking

Release compatible with all major OS both in cli and GUI format.

__N.B.__ Chromium browser is required. If you have Google Chrome installed you already have it.

A problem with macOS ssl certificates has already been identified on macOS > 11. As a temporary workaround use source with Python 3.7 or higher.

With a terminal open on the base repository path and python 3.7 or higher installed type  
```python -m venv venv```  
```source venv/bin/activate```  
```pip install -r requirements.txt```

Then run `main.py` for CLI interface, `main_gui.py` for a chromium based GUI.
