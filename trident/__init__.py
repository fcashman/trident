"""
Trident is a python-based package extending yt for generating synthetic
observations of hydrodynamical datasets.

Please visit the Trident and yt websites for more information:
http://trident-project.org
http://yt-project.org
"""

# Import all structures from trident.py
from code import *

# Import modified_ion_balance functions
from modified_ion_balance.cloudy_ion_balance import \
    add_Cloudy_ion_number_density_field, \
    add_Cloudy_ion_density_field, \
    add_Cloudy_ion_fraction_field

from modified_ion_balance.modify_light_rays import \
    add_ion_fields_to_ray, \
    add_ion_fields_to_file

from ion_balance.ion_balance import *

# Import yt's LightRay class
from yt.analysis_modules.cosmological_observation.api import LightRay
