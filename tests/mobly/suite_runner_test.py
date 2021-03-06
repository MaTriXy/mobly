#!/usr/bin/env python3.4
#
# Copyright 2017 Google Inc.
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
import unittest

from mobly import suite_runner

from tests.lib import integration_test
from tests.lib import integration2_test


class SuiteRunnerTest(unittest.TestCase):
    def test_select_no_args(self):
        identifiers = suite_runner._compute_test_identifiers(
            test_classes=[
                integration_test.IntegrationTest,
                integration2_test.Integration2Test
            ],
            selected_test_cases=None)
        self.assertEqual(
            [('IntegrationTest', None), ('Integration2Test', None)],
            identifiers)

    def test_select_by_class(self):
        identifiers = suite_runner._compute_test_identifiers(
            test_classes=[
                integration_test.IntegrationTest,
                integration2_test.Integration2Test
            ],
            selected_test_cases=['IntegrationTest'])
        self.assertEqual([('IntegrationTest', None)], identifiers)

    def test_select_by_method(self):
        identifiers = suite_runner._compute_test_identifiers(
            test_classes=[
                integration_test.IntegrationTest,
                integration2_test.Integration2Test
            ],
            selected_test_cases=[
                'IntegrationTest.test_a', 'IntegrationTest.test_b'
            ])
        self.assertEqual([('IntegrationTest', ['test_a', 'test_b'])],
                         identifiers)

    def test_select_all_clobbers_method(self):
        identifiers = suite_runner._compute_test_identifiers(
            test_classes=[
                integration_test.IntegrationTest,
                integration2_test.Integration2Test
            ],
            selected_test_cases=['IntegrationTest.test_a', 'IntegrationTest'])
        self.assertEqual([('IntegrationTest', None)], identifiers)

        identifiers = suite_runner._compute_test_identifiers(
            test_classes=[
                integration_test.IntegrationTest,
                integration2_test.Integration2Test
            ],
            selected_test_cases=['IntegrationTest', 'IntegrationTest.test_a'])
        self.assertEqual([('IntegrationTest', None)], identifiers)


if __name__ == "__main__":
    unittest.main()
