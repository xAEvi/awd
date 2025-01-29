from ..Services.get_vehicles_service import GetVehiclesService

def load_routes(api):
    api.add_resource(GetVehiclesService, '/vehicles/')