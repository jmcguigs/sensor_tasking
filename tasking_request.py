from pydantic import BaseModel
from enum import Enum
from typing import Union
from datetime import datetime


class CollectionType(Enum):
    # type of sensor to use during the collection
    OPTICAL = 0
    PASSIVE_RF = 1


class TargetType(Enum):
    # type of target to collect data on
    SATELLITE = 0
    RADEC = 1
    PLANET = 2


class RFParameters(BaseModel):
    rf_center_frequency: float      # center frequency of the RF collection in Hz
    rf_bandwidth: float             # bandwidth of the RF collection in Hz
    rf_polarization: str            # polarization of the RF collection
    rf_gain: float                  # gain of the RF collection in dB


class OpticalParameters(BaseModel):
    eo_exposure_time: float         # exposure time of the optical collection in seconds
    eo_optical_gain: float          # gain of the optical collection (unitless)
    eo_filter: Union[str, None]     # filter used for the optical collection


class RADEC(BaseModel):
    # right ascension and declination of the target in degrees
    ra: float
    dec: float

class SolarSystemObject(BaseModel):
    # name of the solar system object, to be used as a key to look up the object's ephemeris
    name: str


class SatelliteElementSet(BaseModel):
    # storage class for satellite element set data
    name: str
    norad_id: int
    classification_type: str
    epoch: str
    mean_motion_derivative: float
    mean_motion_sec_derivative: float
    bstar: float
    inclination: float
    right_ascension: float
    eccentricity: float
    argument_of_perigee: float
    mean_anomaly: float
    mean_motion: float
    revolutions_at_epoch: int


class TaskingRequest(BaseModel):
    # required parameters
    task_id: int                        # unique identifier for this tasking request
    priority: int                       # priority of this tasking request
    originator: str                     # name of the entity that originated this tasking request
    tasking_start_time: datetime        # start time of the tasking request
    tasking_end_time: datetime          # end time of the tasking request
    collection_type: CollectionType     # type of collection requested
    target_type: TargetType             # type of target being collected

    # additional parameters based on target type
    target: Union[SatelliteElementSet, RADEC, SolarSystemObject]

    # additional parameters based on collection type
    collection_params: Union[RFParameters, OpticalParameters]
