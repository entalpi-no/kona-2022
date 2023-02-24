# Entalpi public dataset Kona 2022

![Gustav and Kristian pondering on their data](entalpi-212.jpg)

## About Entalpi
After years of coaching top athletes to world class results and world records, we launched an ambition to make our state of the art training method and sports technology available for athletes all over the world. With [Entalpi](https://entalpi.com) our ambition is to break both personal and world records and to change the way athletes train. Welcome to a new era where training, technology and big data is combined in a new and unique way to push human limits to new heights!


## About the dataset
This repository contains a dataset with data from Gustav Iden's and Kristian Blummenfelt's run on the 2022 Ironman world championship in Kona.
All the data in this repository is published under the "Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)" license. For more information about this license, read the full license [here](LICENSE) or more information about it [here](https://creativecommons.org/licenses/by-nc/4.0/).

The dataset is made publicly available as we use it during the application process of hiring new team members for Entalpi. You can find our open positions [here](https://www.entalpi.com/careers).
If you are not currently applying for a job at Entalpi (but if you are reading this, you probably should!) we still welcome you to explore and play around with the dataset and share the results (also with us if you find something interesting 🤓), but make sure that you adhere to the license referenced above.


## Description of the dataset
This repository contains data from Gustav's and Kristian's run during the 2022 Ironman world championships.
The data was recorded on their sport watches. Not all the data that was collected is published, for privacy and competive reasons.
The data that is published is:
- speed [m/s]
- cadence [/min]
- stride length [m]
- heartrate [bpm]
- elevation [m]
- gps location (latitude and longitude) [°]
- core temperature [°C] (only for Kristian)
- skin temperature [°C] (only for Kristian)

The data from both athletes is stored in 2 separate .csv files ([Gustav](./gustav_iden_copyright_entalpi_as.csv), [Kristian](./kristian_blummenfelt_copyright_entalpi_as.csv)) that are identical in format (order of columns might differ):
```csv
datetime,latitude,longitude,speed,elevation,heartrate,cadence,core_temperature,skin_temperature,stride_length
2022-10-08 21:27:33+00:00,19.63866636157036,-155.9970761463046,4.012,9.199999999999989,140.0,89.0,38.86000061035156,34.20000076293945,1.406
2022-10-08 21:27:34+00:00,19.63863903656602,-155.99709006026387,4.012,9.199999999999989,140.0,89.0,38.86000061035156,34.20000076293945,1.4
2022-10-08 21:27:35+00:00,19.6386088617146,-155.99710405804217,4.003,9.199999999999989,139.0,89.0,38.86000061035156,34.20000076293945,1.409
...
```

## Contact
For information about Entalpi or this dataset, you can [contact us here](https://www.entalpi.com/contact-us).
For information about working at Entalpi, please contact us at jobs@entalpi.com.


## Technical documentation

The `./scripts/` directory contains a `fit_to_csv.py` file that is used to convert the source .fit files to .csv files.

To convert .fit files to .csv files, clone this repository, `cd` into it's directory and then run these commands in order:

```shell
cd scripts
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m fit_to_csv {fit_file_path} {csv_file_path}
```

Please note that this requires a recent version of Python installed on your computer.
