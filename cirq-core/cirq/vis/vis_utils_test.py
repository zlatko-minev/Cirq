# Copyright 2021 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import numpy as np

import cirq


def test_relative_luminance() -> None:
    rl = cirq.vis.relative_luminance([100, 100, 100])
    assert np.isclose(rl, 55560.6360)
    rl = cirq.vis.relative_luminance([0, 1, 2])
    assert np.isclose(rl, 1.0728676632649454)
    rl = cirq.vis.relative_luminance(np.array([0, 1, 2]))
    assert np.isclose(rl, 1.0728676632649454)
