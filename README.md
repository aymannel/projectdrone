## Description
- `main.py` generates `drone_coords.csv` from `drone_coords.SRT`
- `drone_coords.csv` contains `frame_num`, `longitude`, `latitude` and `is_reference` flag

|frame_num|drone_latitude               |drone_longitude|displacement_origin                          |displacement_previous|drone_latitude_pixels|drone_longitude_pixels|displacement_origin_pixels|displacement_previous_pixels|is_reference|
|---------|-----------------------------|---------------|---------------------------------------------|---------------------|---------------------|----------------------|--------------------------|----------------------------|------------|
|1        |38.012993                    |23.753021      |                                             |                     |                     |                      |                          |                            |True        |
|2        |38.012993                    |23.753021      |                                             |                     |                     |                      |                          |                            |False       |
|3        |38.012993                    |23.753021      |                                             |                     |                     |                      |                          |                            |False       |
|4        |38.012993                    |23.753021      |                                             |                     |                     |                      |                          |                            |False       |

## To Do
- calculate `displacement_from_origin` and `displacement_from_previous`
- calculate conversion from longitude/latitude to pixels
