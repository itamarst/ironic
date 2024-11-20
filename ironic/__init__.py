# Always use eventlet's asyncio hub, so as to ensure compatibility with
# asyncio-based libraries.
import os
os.environ["EVENTLET_HUB"] = "asyncio"
del os
