import multiprocessing

def calculate_room_area(width, length, height, output_file):
    area = 2 * height * (width + length)
    with open(output_file, 'a') as f:
        f.write(f"Area of the room: {area} sq.m\n")

def calculate_paint_consumption(width, length, height, output_file):
    area = 2 * height * (width + length)
    consumption = area / 5
    with open(output_file, 'a') as f:
        f.write(f"Paint consumption: {consumption} L\n")

if __name__ == '__main__':
    width, length, height = 3, 4, 2.5
    output_file = "room_data.txt"
    with multiprocessing.Pool(processes=2) as pool:
        pool.apply_async(calculate_room_area, args=(width, length, height, output_file))
        pool.apply_async(calculate_paint_consumption, args=(width, length, height, output_file))
        pool.close()
        pool.join()
