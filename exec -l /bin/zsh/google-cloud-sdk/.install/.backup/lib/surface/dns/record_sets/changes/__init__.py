# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""gcloud dns record-sets changes command group."""

from googlecloudsdk.calliope import base


class Changes(base.Group):
  """View details about changes to your Cloud DNS record-sets."""

  detailed_help = {
      'DESCRIPTION': '{description}',
      'EXAMPLES': """\
          To view the details of a particular change, run:

            $ {command} describe CHANGE_ID -z MANAGED_ZONE

          To view the list of all changes, run:

            $ {command} list -z MANAGED_ZONE
          """,
  }
