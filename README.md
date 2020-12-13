#### Introduction

The `biokinepy` library provides utilities for processing, computing, and analyzing joint kinematics - although at the moment it is not comprehensive. It aims to provide a starting point for creating a comprehensive Python library for analyzing motion capture datasets.

#### Installation

`pip install biokinepy`

#### Vision

`biokinepy` processing starts with either skin marker trajectories or segment kinematics. It does NOT derive skin marker trajectories from videos, nor does it derive segment kinematics from biplane recordings. These tasks have already been implemented by other utilities, or are fulfilled by software supplied by the manufacturer (e.g. [Vicon](https://www.vicon.com/)). What is missing in the Python ecosystem is a comprehensive library for analyzing motion capture datasets, which is where `biokinepy` comes in. Tools such as [Visual3D](https://c-motion.com/products/visual3d) currently fulfill this function but 1) are not free, 2) are not open-source, 3) are inflexible, 4) are now outdated.

Current research efforts both within biomechanics and computer science community focus on new methods for:

* Filling occluded marker trajectories
* Attenuating the effect of soft tissue artefact
* Computing the center of rotation of joints from noisy data
* Filtering/smoothing marker trajectories and segment kinematics (not a trivial task since rotations do not form a vector space)
* Analyzing joint kinematic trajectories in terms of Euler angles, helical angles, etc.

The vision for `biokinepy` is to provide a central library where all the aforementioned algorithms are implemented. This gives researchers the ability to:

* Implement custom motion capture processing pipelines by picking the algorithms they deem appropriate
* Compare and contrast the effects of various algorithms on their dataset
* Easily share new algorithms

The current version of `biokinepy` is nowhere close to fulfilling the goals outlined above, but hopefully one day it (or another package) will.

#### Summary of current implementation

* `absor` - methods for computing the kinematics of a segment from the trajectories of the markers that were attached to it.
* `cs` -  methods for manipulating homogeneous transformation matrices.
* `euler_angles` - methods for computing Euler angle trajectories from rotation matrices, currently only shoulder relevant Euler angle sequences have been implemented.
* `filling` - methods for filling occluded skin marker trajectories, currently only rigid body filling is implemented.
* `joint_center` - methods for computing the joint center of rotation from skin marker trajectories, currently only one method is implemented.
* `segment_cs` - methods for establishing the anatomical coordinate of segments, currently only the International Society of Biomechanics scapula definition is implemented.
* `mean_smoother` - mean smoother for position and orientation (using quaternions for averaging).
* `np_utils` - set of utilities for `numpy`.
* `trajectory` - a class that represents a rigid body trajectory and provides easy access to methods for analyzing the trajectory.
* `vec_ops` - common vector operations.
* `vel_acc` - code for computing (angular) velocity and acceleration from a rotation matrix trajectory.