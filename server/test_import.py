#!/usr/bin/env python
import sys
import traceback
sys.path.insert(0, '.')

print("=" * 60)
print("TEST 1: Direct execution of wavelet.py code")
print("=" * 60)
try:
    exec(open('wavelet.py').read())
    print("SUCCESS: wavelet.py code executed directly")
except Exception as e:
    print(f"FAILED: {e}")
    traceback.print_exc()

print("\n" + "=" * 60)
print("TEST 2: Import wavelet module")
print("=" * 60)
try:
    import wavelet
    print(f"Module imported. Attributes: {dir(wavelet)}")
    if 'w2d' in dir(wavelet):
        print("SUCCESS: w2d function found in wavelet module")
    else:
        print("FAILED: w2d function NOT found in wavelet module")
except Exception as e:
    print(f"FAILED: {e}")
    traceback.print_exc()

print("\n" + "=" * 60)
print("TEST 3: Import w2d from wavelet")
print("=" * 60)
try:
    from wavelet import w2d
    print("SUCCESS: w2d imported from wavelet")
except Exception as e:
    print(f"FAILED: {e}")
    traceback.print_exc()

print("\n" + "=" * 60)
print("TEST 4: Import util")
print("=" * 60)
try:
    import util
    print("SUCCESS: util imported")
    util.load_saved_artifacts()
    print("SUCCESS: Artifacts loaded")
except Exception as e:
    print(f"FAILED: {e}")
    traceback.print_exc()
