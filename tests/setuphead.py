#!/usr/bin/env python3
import os, sys, time, imp

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
set_env = imp.load_source(
    "set_env",
    os.path.join(ROOT_DIR, "set_env.py")
)
try:
    set_env.activate_venv()
except set_env.SFToolsError as err:
    sys.exit(str(err))