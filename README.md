# Sensor Tasking Format for Optical & Radio Astronomy Observatories

### Designed for use with REST APIs for tasking remote observatories

#### Tasking Requests
The `TaskingRequest` class contains required and optional fields for requesting an EO/RF observatory
collect on a target.

Requied parameters:
1. `task_id`: a unique ID for the tasking request, required by the REST API
2. `priority`: a priority assigned to the collect- used to de-conflict if two tasks overlap
3. `originator`: the name of the requestor
4. `tasking_start_time`: the UTC datetime when the tasking is relevant (not necessarily when a given observation window opens)
5. `tasking_end_time`: the UTC datetime when the tasking request expires (not necessarily when a given observation window ends)
6. `collection_type`: enum corresponding to the type of collect (0: optical, 1: passive RF)
    - One set of either `RFParameters` or `OpticalParameters` depending on the collection type is required.
7. `target_type`: enum corresponding to the type of target (0: satellite, 1: RADEC sky coordinate, 2: planet)
    - One set of `SatelliteElementSet`, `RADEC`, or `SolarSystemObject` is required, depending on target type.



