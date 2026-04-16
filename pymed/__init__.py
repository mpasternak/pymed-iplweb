from importlib.metadata import version

from .api import PubMed

__version__ = version("pymed-iplweb")

__all__ = ["PubMed", "__version__"]
