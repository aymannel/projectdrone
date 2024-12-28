## Description
- `main.py` generates `drone_coords.csv` from `drone_coords.SRT`
- `drone_coords.csv` contains `frame_num`, `longitude`, `latitude` and `is_reference` flag
- `index` (0, 1, 2...)
- `frame = index + 1` (1, 2, 3...)

|frame_number|latitude |longitude|displacement_previous|latitude_pixels|longitude_pixels|displacement_previous_pixels|is_reference|
|------------|---------|---------|---------------------|---------------|----------------|----------------------------|------------|
|1           |38.012993|23.753021|(0, 0)               |               |                |                            |True        |
|299         |38.013697|23.753369|(7.000000003642981e-06, 2.9999999995311555e-06)|               |                |                            |False       |
|549         |38.014368|23.753697|(6.999999996537554e-06, 2.9999999995311555e-06)|               |                |                            |False       |
|799         |38.015038|23.754025|(6.999999996537554e-06, 2.9999999995311555e-06)|               |                |                            |False       |
|1049        |38.015708|23.754355|(5.999999999062311e-06, 2.9999999995311555e-06)|               |                |                            |False       |

## To Do
- calculate `displacement_from_origin` and `displacement_from_previous`
- calculate conversion from longitude/latitude to pixels
