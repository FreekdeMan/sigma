# Output backends for sigmac
# Copyright 2016-2017 Thomas Patzke, Florian Roth, Ben de Haan, Devin Ferguson

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import json
import re
import sigma

class GraylogQuerystringBackend(SingleTextQueryBackend):
    """Converts Sigma rule into Graylog query string. Only searches, no aggregations."""     
    identifier = "graylog"
    active = True

    reEscape = re.compile("([+\\-!(){}\\[\\]^\"~:/]|\\\\(?![*?])|&&|\\|\\|)")
    reClear = None
    andToken = " AND "
    orToken = " OR "
    notToken = "NOT "
    subExpression = "(%s)"
    listExpression = "(%s)"
    listSeparator = " "
    valueExpression = "\"%s\""
    nullExpression = "NOT _exists_:%s"
    notNullExpression = "_exists_:%s"
    mapExpression = "%s:%s"
    mapListsSpecialHandling = False
