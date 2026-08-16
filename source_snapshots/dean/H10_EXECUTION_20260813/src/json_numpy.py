"""Vendored json_numpy 2.1.1 compatibility module.

Source SHA-256:
4f0ddfe1ab6c57f2dea6967097c9c934cd8f55e9736cd1f54cff844978931bd8
"""

from __future__ import annotations

__version__ = "2.1.1"
__all__ = ["default", "dump", "dumps", "load", "loads", "object_hook", "patch"]

import json
from base64 import b64decode, b64encode
from functools import partial
from typing import TYPE_CHECKING, Any, Callable

from numpy import frombuffer, generic, ndarray
from numpy.lib.format import descr_to_dtype, dtype_to_descr

if TYPE_CHECKING:
    from _typeshed import SupportsRead


def default(
    o: Any, *, fallback_default: Callable[[Any], dict[str, Any]] | None = None
) -> dict[str, Any]:
    if isinstance(o, (ndarray, generic)):
        data = o.data if o.flags["C_CONTIGUOUS"] else o.tobytes()
        return {
            "__numpy__": b64encode(data).decode(),
            "dtype": dtype_to_descr(o.dtype),
            "shape": o.shape,
        }
    if fallback_default is not None:
        return fallback_default(o)
    raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")


def object_hook(dct: dict) -> dict | ndarray | generic:
    if "__numpy__" in dct:
        np_obj = frombuffer(b64decode(dct["__numpy__"]), descr_to_dtype(dct["dtype"]))
        return np_obj.reshape(shape) if (shape := dct["shape"]) else np_obj[0]
    return dct


_default = default
_hook = object_hook
_dumps = json.dumps
_loads = json.loads
_dump = json.dump
_load = json.load


def _patch_encoder(
    *args: Any,
    default: Callable[[Any], Any] | None = None,
    user_cls: type[json.JSONEncoder] | None = None,
    **kwargs: Any,
) -> json.JSONEncoder:
    if user_cls is None:
        user_cls = json.JSONEncoder
    elif default is None:
        encoder = user_cls(*args, **kwargs)
        encoder.default = partial(_default, fallback_default=encoder.default)
        return encoder
    return user_cls(
        *args, default=partial(_default, fallback_default=default), **kwargs
    )


def dumps(*args: Any, cls: type[json.JSONEncoder] | None = None, **kwargs: Any) -> str:
    kwargs["user_cls"] = cls
    return _dumps(*args, cls=_patch_encoder, **kwargs)


def loads(
    *args: Any, object_hook: Callable[[dict], Any] | None = None, **kwargs: Any
) -> Any:
    return _loads(
        *args,
        object_hook=_hook
        if object_hook is None
        else lambda dct: _hook(object_hook(dct)),
        **kwargs,
    )


def dump(*args: Any, cls: type[json.JSONEncoder] | None = None, **kwargs: Any) -> None:
    kwargs["user_cls"] = cls
    return _dump(*args, cls=_patch_encoder, **kwargs)


def load(fp: SupportsRead[str | bytes], **kwargs: Any) -> Any:
    return loads(fp.read(), **kwargs)


def patch() -> None:
    json.dumps = dumps
    json.loads = loads
    json.dump = dump
    json.load = load
