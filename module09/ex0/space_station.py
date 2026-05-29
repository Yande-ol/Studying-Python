from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    try:
        valid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(timezone.utc),
        )
        print("Valid station created:")
        print(f"ID: {valid.station_id}")
        print(f"Name: {valid.name}")
        print(f"Crew: {valid.crew_size} people")
        print(f"Power: {valid.power_level}%")
        print(f"Oxygen: {valid.oxygen_level}%")
        print(
            f"Status: "
            f"{'Operational' if valid.is_operational else 'Non-operational'}"
        )
    except ValidationError as exc:
        print("Unexpected validation error for valid instance:")
        print(exc)

    print("=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="BAD",
            name="Big Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now(timezone.utc),
            notes=None,
        )
    except ValidationError as exc:
        print(exc)


if __name__ == "__main__":
    main()
