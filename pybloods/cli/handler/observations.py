

def create(client, value, unit, extraction_date):
    units = client.units
    observations = client.observations

    unit_resp = units.get(name=unit)
    if len(unit_resp) < 1:
        units.create(name=unit)
        unit_resp = units.get(name=unit)

    response = observations.create(
        value=value,
        unit_id=unit_resp[0]['unit_id'],
        extracted_at=extraction_date
    )

