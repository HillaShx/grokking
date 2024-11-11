from datetime import datetime
from a_sliding_window.averages_of_sub_arrays import solution, input_data


def main():
    for i in input_data.keys():
        start_time = datetime.now()
        result = solution(**input_data[i])
        end_time = datetime.now()
        print(f"input {i} | result: {result} | runtime: {end_time-start_time}")


if __name__ == "__main__":
    main()
