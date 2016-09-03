"""abstract base class for map
using MutableMapping class from collections module for """

from collections.abc import MutableMapping
from Hashes.map_abstract import Map

class MapBase(MutableMapping, Map):
