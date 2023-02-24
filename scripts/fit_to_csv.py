import sys

import sweat


column_translations = {
    "enhanced_speed": "speed",
    "Cadence": "cadence",
    "step_length": "stride_length",
    "enhanced_altitude": "elevation",
}


columns_of_interest = [
    "enhanced_speed",
    "Cadence",
    "cadence",
    "step_length",
    "heartrate",
    "enhanced_altitude",
    "latitude",
    "longitude",
    "core_temperature",
    "skin_temperature",
]


def fit_to_csv(fit_path, out_path):
    activity = sweat.read_fit(fit_path)

    activity = activity[activity.columns.intersection(columns_of_interest)]
    if "cadence" in activity.columns and "Cadence" in activity.columns:
        del activity["Cadence"]

    activity = activity.rename(
        columns=column_translations,
    )

    # Convert stride length from mm to m.
    activity["stride_length"] = activity["stride_length"] / 1000.0

    activity.to_csv(out_path)


if __name__ == "__main__":
    fit_path = sys.argv[1]
    out_path = sys.argv[2]

    fit_to_csv(fit_path, out_path)
