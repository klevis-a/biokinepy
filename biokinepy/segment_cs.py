import numpy as np


def scapula_cs_isb(ac_gc: np.ndarray, ia: np.ndarray, ts: np.ndarray) -> np.ndarray:
    """Return scapula frame (ISB) given landmarks."""
    z_axis = ac_gc - ts
    x_axis = np.cross(z_axis, ia - ts)
    y_axis = np.cross(z_axis, x_axis)

    x_axis = x_axis/np.linalg.norm(x_axis)
    y_axis = y_axis/np.linalg.norm(y_axis)
    z_axis = z_axis/np.linalg.norm(z_axis)

    scap = np.eye(4)
    scap[0:3, 0] = x_axis
    scap[0:3, 1] = y_axis
    scap[0:3, 2] = z_axis
    scap[0:3, 3] = ac_gc

    return scap