"""
Copyright (c) 2022 Ruilong Li, UC Berkeley.
"""

from typing import Any, Callable


def _make_lazy_cuda_func(name: str) -> Callable:
    def call_cuda(*args, **kwargs):
        # pylint: disable=import-outside-toplevel
        from ._backend import _C

        return getattr(_C, name)(*args, **kwargs)

    return call_cuda


is_cub_available = _make_lazy_cuda_func("is_cub_available")

# data specs
MultiScaleGridSpec = _make_lazy_cuda_func("MultiScaleGridSpec")
RaysSpec = _make_lazy_cuda_func("RaysSpec")
RaySegmentsSpec = _make_lazy_cuda_func("RaySegmentsSpec")

# grid
ray_aabb_intersect = _make_lazy_cuda_func("ray_aabb_intersect")
traverse_grids = _make_lazy_cuda_func("traverse_grids")

# scan
exclusive_sum_by_key = _make_lazy_cuda_func("exclusive_sum_by_key")
inclusive_sum = _make_lazy_cuda_func("inclusive_sum")
exclusive_sum = _make_lazy_cuda_func("exclusive_sum")
inclusive_prod_forward = _make_lazy_cuda_func("inclusive_prod_forward")
inclusive_prod_backward = _make_lazy_cuda_func("inclusive_prod_backward")
exclusive_prod_forward = _make_lazy_cuda_func("exclusive_prod_forward")
exclusive_prod_backward = _make_lazy_cuda_func("exclusive_prod_backward")

# pdf
importance_sampling = _make_lazy_cuda_func("importance_sampling")
searchsorted = _make_lazy_cuda_func("searchsorted")
