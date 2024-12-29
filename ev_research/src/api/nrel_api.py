"""NREL API client for accessing EV charging station data."""

import aiohttp
from typing import Dict, List, Any
from ..models.data_models import ChargingStation
from ..config.settings import NREL_API_KEY, NREL_STATION_SEARCH_ENDPOINT

class NRELAPIClient:
    """Client for interacting with the NREL Alternative Fuels Data Center API."""
    
    def __init__(self, api_key: str = NREL_API_KEY):
        """Initialize the NREL API client."""
        self.api_key = api_key
        self.base_params = {
            "api_key": self.api_key,
            "fuel_type": "ELEC",
            "status": "all",
            "access": "all",
        }
    
    async def get_stations(self, location: str) -> List[ChargingStation]:
        """
        Fetch EV charging stations for a given location.
        
        Args:
            location: Location string (e.g. "city, state")
            
        Returns:
            List of ChargingStation objects
        """
        params = {
            **self.base_params,
            "location": location,
            "limit": "all"
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(NREL_STATION_SEARCH_ENDPOINT, params=params) as response:
                if response.status != 200:
                    raise Exception(f"NREL API request failed: {await response.text()}")
                
                data = await response.json()
                return self._parse_stations(data["fuel_stations"])
    
    def _parse_stations(self, stations_data: List[Dict[str, Any]]) -> List[ChargingStation]:
        """Parse raw station data into ChargingStation objects."""
        stations = []
        for station in stations_data:
            connector_types = []
            if station.get("ev_connector_types"):
                connector_types = station["ev_connector_types"]
            
            stations.append(ChargingStation(
                station_id=str(station["id"]),
                name=station["station_name"],
                latitude=station["latitude"],
                longitude=station["longitude"],
                address=station["street_address"],
                city=station["city"],
                state=station["state"],
                zip_code=station["zip"],
                status=station["status_code"],
                access_type=station["access_code"],
                connector_types=connector_types,
                network=station.get("ev_network"),
                hours=station.get("access_days_time"),
                pricing=station.get("ev_pricing")
            ))
        
        return stations
