# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for Maxout layer."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

from tensorflow_addons.layers.python.maxout import Maxout
from tensorflow_addons.utils.python import test_utils


@test_utils.run_all_in_graph_and_eager_modes
class MaxOutTest(tf.test.TestCase):
    def test_simple(self):
        test_utils.layer_test(
            Maxout, kwargs={'num_units': 3}, input_shape=(5, 4, 2, 18))

    def test_nchw(self):
        test_utils.layer_test(
            Maxout,
            kwargs={
                'num_units': 4,
                'axis': 1
            },
            input_shape=(2, 20, 3, 6))

        test_utils.layer_test(
            Maxout,
            kwargs={
                'num_units': 4,
                'axis': -3
            },
            input_shape=(2, 20, 3, 6))

    def test_unknown(self):
        inputs = np.random.random((5, 4, 2, 18)).astype('float32')
        test_utils.layer_test(
            Maxout,
            kwargs={'num_units': 3},
            input_shape=(5, 4, 2, None),
            input_data=inputs)

        test_utils.layer_test(
            Maxout,
            kwargs={'num_units': 3},
            input_shape=(None, None, None, None),
            input_data=inputs)

    def test_invalid_shape(self):
        with self.assertRaisesRegexp(ValueError, r'number of features'):
            test_utils.layer_test(
                Maxout, kwargs={'num_units': 3}, input_shape=(5, 4, 2, 7))


if __name__ == '__main__':
    tf.test.main()
