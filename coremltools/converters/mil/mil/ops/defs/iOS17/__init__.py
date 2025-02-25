#  Copyright (c) 2022, Apple Inc. All rights reserved.
#
#  Use of this source code is governed by a BSD-3-clause license that can be
#  found in the LICENSE.txt file or at https://opensource.org/licenses/BSD-3-Clause

from coremltools.converters.mil._deployment_compatibility import AvailableTarget as target

_IOS17_TARGET = target.iOS17

from .activation import (
    clamped_relu,
    elu,
    leaky_relu,
    linear_activation,
    prelu,
    scaled_tanh,
    sigmoid_hard,
    softplus_parametric,
    thresholded_relu,
)
from .elementwise_unary import cast, clip
from .image_resizing import crop_resize
from .quantization_ops import dequantize, quantize
from .reduction import reduce_argmax, reduce_argmin
from .scatter_gather import (
    gather,
    gather_along_axis,
    gather_nd,
    scatter,
    scatter_along_axis,
    scatter_nd,
)
from .tensor_operation import non_maximum_suppression, topk
from .tensor_transformation import reshape
