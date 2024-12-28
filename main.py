import re
import csv

reference_frames = [1, 300, 550, 800, 1050, 1300, 1550, 1800, 2050, 2350, 2600, 2900, 3200, 3500, 3800, 4100, 4350, 4600, 4900, 5150, 5400, 5650, 6050, 6300, 6550, 6800]

def extract_coords(coord):
    regex = r"\[latitude\s*:\s*([-\d.]+)\]\s*\[longtitude\s*:\s*([-\d.]+)\]"
    match = re.search(regex, coord)
    if match:
        latitude, longitude = float(match.group(1)), float(match.group(2))
        return (latitude, longitude)

with open('drone_coords.SRT', 'r') as file:
    drone_coords_file = file.read()
    raw_coords = [c for c in drone_coords_file.split('\n\n') if c]
    drone_coords = [extract_coords(r) for r in raw_coords]

def calculate_displacement_vector(index):
    if index == 0:
        return (0, 0)
    else:
        long_curr = drone_coords[index][0]
        long_prev = drone_coords[index - 1][0]
        lat_curr = drone_coords[index][1]
        lat_prev = drone_coords[index - 1][1]
        return ((long_curr - long_prev), (lat_curr - lat_prev))

with open('drone_coords.csv', 'w', newline='') as file:
    columns = [[
        'frame_number',
        'latitude',
        'longitude',
        'displacement_previous',
        'latitude_pixels',
        'longitude_pixels',
        'displacement_previous_pixels',
        'is_reference'
        ]]

    data = [[index + 1,
            coords[0],
            coords[1],
            calculate_displacement_vector(index),
            None,
            None,
            None,
            index + 1 in reference_frames]
            for index, coords in enumerate(drone_coords)]

    writer = csv.writer(file)
    writer.writerows(columns + data)

