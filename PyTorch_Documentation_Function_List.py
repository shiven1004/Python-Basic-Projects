# Import the PyTorch library
import torch

# Returns the number of available MPS devices.
"""
print(torch.mps.device_count())
"""

# Waits for all kernels in all streams on a MPS device to complete.
"""
torch.mps.sunchronize()             
"""

# Returns the random number generator state ad a ByteTensor.
"""
print(torch.mps.get_rng_state())
"""

# Sets the random number generator state.
"""
torch.mps.set_rng_state()           
"""

# Sets the seed for generating random numbers to a random number.
"""
torch.mps.manual_seed()             
"""

# Sets the seed for generating random numbers to a random number.
"""
torch.mps.seed()                    
"""

# Releases all unoccupied cached memory currently held by the
"""
torch.mps.empty_cache()             
"""

# Set memory fraction for limiting process's memory allocation on MPS device.
"""
torch.mps.set_per_process_memory_fraction()
"""

# Returns the current GPU memory occupied by tensors in bytes.

torch.mps.current_allocated_memory()


# Returns total GPU memory allocated by Metal driver for process in bytes.
"""
torch.mps.driver_allocated_memory()
"""

# Returns recommended max Working set size for GPU memory in bytes.
"""
torch.mps.recommended_max_memory()
"""

# Compiles compute shader from source and allows one to invoke kernels defined there from the confort of Python runtime Example.
"""
torch.mps.compile_shader()
"""

# MPS Profiler:

# Start OS Signpost tracing from MPS backend.
"""
torch.mps.profirler.start()
"""

# Stops generating OS Signpost tracing from MPS backend.
"""
torch.mps.profiler.stop()
"""

# Context Manager to enabling generating OS Signpost tracing from MPS backend.
"""
torch.mps.profiler.profile()
"""

# Checks id metal capture is in progress.
"""
torch.mps.profiler.is_capturing_metal()
"""

# Checks if metal_capture context manager is usable To enable metal capture, set MTL_CAPTURE_ENABLED envvar.
"""
torch.mps.profiler.is_metal_capture_enabled()
"""

# Context manager that enables capturing of Metal calls into gputrace.
"""
torch.mps.metal_capture()
"""

# MPS Event:

# Wrapper aroung an MPS event.
"""
torch.mps.event.Event()
"""
