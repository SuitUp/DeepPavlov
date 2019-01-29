# Copyright 2017 Neural Networks and Deep Learning lab, MIPT
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


from typing import List, Union
from operator import itemgetter

import pickle
import numpy as np

from deeppavlov.core.commands.utils import expand_path
from deeppavlov.core.common.registry import register
from deeppavlov.core.common.log import get_logger
from deeppavlov.core.models.estimator import Component
from deeppavlov.core.common.chainer import Chainer

logger = get_logger(__name__)


@register("search_predictor")
class SearchPredictor(Component):

    def __init__(self,
                 **kwargs):
        pass


    def __call__(self, responses, preds):
        sorted_ids = np.flip(np.argsort(preds[0]), -1)
        return [responses[0][sorted_ids[0]]]