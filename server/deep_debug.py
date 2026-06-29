import sys
import os

print("Python version:", sys.version)
print("Working dir:", os.getcwd())

# Import wavelet manually
print("\n--- Step 1: Read wavelet.py file ---")
with open('wavelet.py', 'r') as f:
    content = f.read()
print(f"File size: {len(content)} bytes")
print("First 100 chars:", repr(content[:100]))

# Create namespace and execute
print("\n--- Step 2: Execute wavelet.py in isolated namespace ---")
namespace = {}
try:
    exec(content, namespace)
    print(f"SUCCESS: Execution completed")
    print(f"Namespace keys: {list(namespace.keys())}")
    if 'w2d' in namespace:
        print("w2d function found!")
        print(f"w2d: {namespace['w2d']}")
    else:
        print("ERROR: w2d not in namespace!")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()

# Now try normal import
print("\n--- Step 3: Try normal import ---")
try:
    import wavelet
    print(f"Module attributes: {[x for x in dir(wavelet) if not x.startswith('_')]}")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
