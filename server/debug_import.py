import sys
sys.path.insert(0, '.')

# Try importing wavelet step by step
try:
    import numpy as np
    print("1. numpy - OK")
except Exception as e:
    print(f"1. numpy - FAILED: {e}")

try:
    import pywt
    print("2. pywt - OK")
except Exception as e:
    print(f"2. pywt - FAILED: {e}")

try:
    import cv2
    print("3. cv2 - OK")
except Exception as e:
    print(f"3. cv2 - FAILED: {e}")

# Now try wavelet with verbose error handling
print("\n--- Importing wavelet ---")
import importlib.util
spec = importlib.util.spec_from_file_location("wavelet", "wavelet.py")
wavelet_mod = importlib.util.module_from_spec(spec)

try:
    spec.loader.exec_module(wavelet_mod)
    print("Wavelet module loaded successfully!")
    print(f"Module attributes: {dir(wavelet_mod)}")
except Exception as e:
    print(f"Failed to load wavelet module: {e}")
    import traceback
    traceback.print_exc()
