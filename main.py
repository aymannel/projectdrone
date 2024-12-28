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

with open('drone_coords.csv', 'w', newline='') as file:
    columns = [['frame_num', 'drone_latitude', 'drone_longitude', 'is_reference']]
    data = [[frame + 1, *coords, frame + 1 in reference_frames] for frame, coords in enumerate(drone_coords)]
    writer = csv.writer(file)
    writer.writerows(columns + data)

