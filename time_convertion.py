FORMAT_PM = "PM"
FORMAT_AM = "AM"
INSTANCE_STR = ""


def time_convertion(data: str):
    time = [t for t in data]

    format_hour = INSTANCE_STR.join(time[-2:])

    if format_hour == FORMAT_AM:
        hour_input = int(INSTANCE_STR.join(time[:2]))

        # Format hour to output
        hour_formatted = time[2:]
        value = 0
        if hour_input < 12:
            hour_output = hour_input
            if hour_output <= 9:
                value = f'0{hour_output}'
            else:
                value = hour_output
        elif hour_input >= 12:
            hour_output = abs(hour_input-12)
            if hour_output <= 9:
                value = f'0{hour_output}'
            else:
                value = hour_output

        hour_formatted.insert(0, str(value))
        hour_str = INSTANCE_STR.join(hour_formatted)

        return hour_str.replace(FORMAT_AM, INSTANCE_STR)

    if format_hour == FORMAT_PM:
        hour_input = int(INSTANCE_STR.join(time[:2]))
        hour_output = 12 + hour_input if hour_input < 12 else hour_input

        # Format hour to output
        hour_formatted = time[2:]
        hour_formatted.insert(0, str(hour_output))
        hour_str = INSTANCE_STR.join(hour_formatted)

        return hour_str.replace(FORMAT_PM, INSTANCE_STR)


if __name__ == "__main__":
    r = time_convertion("04:59:59AM")
    print(r)
