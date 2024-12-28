## Description
- `main.py` generates `drone_coords.csv` from `drone_coords.SRT`
- `drone_coords.csv` contains `frame_num`, `longitude`, `latitude` and `is_reference` flag

|frame_num|drone_latitude               |drone_longitude|is_reference                                 |
|---------|-----------------------------|---------------|---------------------------------------------|
|1        |38.012993                    |23.753021      |True                                         |
|2        |38.012993                    |23.753021      |False                                        |
|3        |38.012993                    |23.753021      |False                                        |
|4        |38.012993                    |23.753021      |False                                        |
|5        |38.012993                    |23.753021      |False                                        |
|6        |38.012993                    |23.753022      |False                                        |

## To Do
- calculate `displacement_from_origin` and `displacement_from_previous`
- calculate conversion from longitude/latitude to pixels
