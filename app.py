"""Root Streamlit launcher.

Render uses app/app.py, but this file lets evaluators run:
streamlit run app.py
"""

from runpy import run_path
from pathlib import Path


run_path(str(Path(__file__).resolve().parent / "app" / "app.py"), run_name="__main__")
