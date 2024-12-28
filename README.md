## Description
- `main.py` generates `drone_coords.csv` from `drone_coords.SRT`
- `drone_coords.csv` contains `frame_num`, `longitude`, `latitude` and `is_reference` flag
- `index` (0, 1, 2...)
- `frame = index + 1` (1, 2, 3...)

|frame_number|latitude |longitude|displacement_previous|latitude_pixels|longitude_pixels|displacement_previous_pixels|is_reference|
|------------|---------|---------|---------------------|---------------|----------------|----------------------------|------------|
|1           |38.012993|23.753021|(0, 0)               |               |                |                            |True        |
|2           |38.012993|23.753021|(0.0, 0.0)           |               |                |                            |False       |
|3           |38.012993|23.753021|(0.0, 0.0)           |               |                |                            |False       |
|4           |38.012993|23.753021|(0.0, 0.0)           |               |                |                            |False       |
|5           |38.012993|23.753021|(0.0, 0.0)           |               |                |                            |False       |

## To Do
- calculate `displacement_from_origin` and `displacement_from_previous`
- calculate conversion from longitude/latitude to pixels
