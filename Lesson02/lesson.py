import yaml
import pprint

car_details = yaml.load("""
    name: Mustang
    year: 2016
    manufacturer: Ford
    epa_mileage_base: [17, 28]
    drive_type: rwd
    wheelbase: 107.1
    trim_levels:
    - Mustang V6
    - Mustang EcoBoost
    - Mustang GT
    - Shelby GT350
    - Shelby GT350R
    """)

pprint.pprint(car_details, indent=2)

