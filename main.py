import numpy as np
import time
import cv2


def find_clockwise(borders, center, i2j2):
    mask = np.array([[1, 1, 1],
                     [1, 0, 1],
                     [1, 1, 1]]).astype('bool')
    roll_dict = {
        (1, 1): 0,
        (1, 0): 1,
        (1, -1): 2,
        (0, -1): 3,
        (-1, -1): 4,
        (-1, 0): 5,
        (-1, 1): 6,
        (0, 1): 7,
    }
    pixel_dict = {
        0: [1, 1],
        1: [1, 0],
        2: [1, -1],
        3: [0, -1],
        4: [-1, -1],
        5: [-1, 0],
        6: [-1, 1],
        7: [0, 1],
    }
    pixel_list = borders[center[0]-1:center[0]+2, center[1]-1:center[1]+2][mask].tolist()
    pixel_list[7], pixel_list[3], pixel_list[6], pixel_list[5], pixel_list[4] =\
        pixel_list[3], pixel_list[4], pixel_list[5], pixel_list[6], pixel_list[7]
    pixel_list = np.roll(pixel_list, -roll_dict[tuple(center - i2j2)])
    pixel_list[pixel_list != 0] = 1
    try:
        if pixel_list.tolist().index(1) + roll_dict[tuple(center - i2j2)] >= 8:
            result = np.array(pixel_dict[pixel_list.tolist().index(1) - 8 + roll_dict[tuple(center - i2j2)]])
        else:
            result = np.array(pixel_dict[pixel_list.tolist().index(1) + roll_dict[tuple(center - i2j2)]])
        return (-result + center).tolist()
    except ValueError:
        return None


def find_counterclockwise(borders, center, i2j2):
    pixel_found = 0
    mask = np.array([[1, 1, 1],
                     [1, 0, 1],
                     [1, 1, 1]]).astype('bool')
    roll_dict = {
        (1, 1): 0,
        (1, 0): 1,
        (1, -1): 2,
        (0, -1): 3,
        (-1, -1): 4,
        (-1, 0): 5,
        (-1, 1): 6,
        (0, 1): 7,
    }
    pixel_dict = {
        0: [1, 1],
        1: [0, 1],
        2: [-1, 1],
        3: [-1, 0],
        4: [-1, -1],
        5: [0, -1],
        6: [1, -1],
        7: [1, 0],
    }
    pixel_list = borders[center[0]-1:center[0]+2, center[1]-1:center[1]+2][mask].tolist()
    pixel_list[7], pixel_list[6], pixel_list[1], pixel_list[5], pixel_list[2], pixel_list[3], pixel_list[4] =\
        pixel_list[1], pixel_list[2], pixel_list[3], pixel_list[4], pixel_list[5], pixel_list[6], pixel_list[7]
    pixel_list = np.roll(pixel_list, roll_dict[tuple(center - i2j2)])
    pixel_list[0] = 0
    pixel_list[pixel_list != 0] = 1
    try:
        if pixel_list.tolist().index(1) - roll_dict[tuple(center - i2j2)] < 0:
            result = np.array(pixel_dict[pixel_list.tolist().index(1) + 8 - roll_dict[tuple(center - i2j2)]])
        else:
            result = np.array(pixel_dict[pixel_list.tolist().index(1) - roll_dict[tuple(center - i2j2)]])
        return (-result + center).tolist(), pixel_found
    except ValueError:
        return None


def find_borders(img):
    nbd = 1
    borders = np.array(img, dtype=int)
    borders[borders == 255] = 1
    for i in range(borders.shape[0]):
        for j in range(borders.shape[1]):
            if borders[i, j] != 0:

                # Step 1, outer border
                if borders[i, j] == 1 and borders[i, j-1] == 0:
                    nbd += 1
                    i2j2 = [i, j-1]
                    # Step 3.1
                    i1j1 = find_clockwise(borders, np.array([i, j]), np.array(i2j2))
                    if i1j1:
                        # Step 3.2
                        i2j2 = i1j1
                        i3j3 = [i, j]
                        # Step 3.3
                        while True:
                            i4j4, next_pixel_found = find_counterclockwise(borders, np.array(i3j3), np.array(i2j2))
                            # Step 3.4
                            if next_pixel_found == 1:
                                borders[i3j3[0], i3j3[1]] = -nbd
                            if next_pixel_found == 0 and borders[i3j3[0], i3j3[1]] == 1:
                                borders[i3j3[0], i3j3[1]] = nbd
                            # Step 3.5
                            if i4j4 == [i, j] and i3j3 == i1j1:
                                break
                            else:
                                i2j2 = i3j3
                                i3j3 = i4j4
                    else:
                        borders[i, j] = -nbd

                # Step 1, Hole border
                elif borders[i, j] >= 1 and borders[i, j+1] == 0:
                    nbd += 1
                    i2j2 = [i, j+1]
                    # Step 3.1
                    i1j1 = find_clockwise(borders, np.array([i, j]), np.array(i2j2))
                    if i1j1:
                        # Step 3.2
                        i2j2 = i1j1
                        i3j3 = [i, j]
                        # Step 3.3
                        while True:
                            i4j4, next_pixel_found = find_counterclockwise(borders, np.array(i3j3), np.array(i2j2))
                            # Step 3.4
                            if next_pixel_found == 1:
                                borders[i3j3[0], i3j3[1]] = -nbd
                            if next_pixel_found == 0 and borders[i3j3[0], i3j3[1]] == 1:
                                borders[i3j3[0], i3j3[1]] = nbd
                            # Step 3.5
                            if i4j4 == [i, j] and i3j3 == i1j1:
                                break
                            else:
                                i2j2 = i3j3
                                i3j3 = i4j4
                    else:
                        borders[i, j] = -nbd

    return borders, nbd


if __name__ == '__main__':
    start_time = time.time()
    image = cv2.imread('image.png', 0)
    image[image == 255] = 1
    border, num = find_borders(image)
    np.savetxt('border.txt', border, fmt=f'%{len(str(num)) + 1}d', )
    border[border < 0] *= -1
    border[border > 1] *= int(255 / num)
    cv2.imwrite('border.png', border)
    print(f'{(time.time() - start_time) * 1000} miliseconds')
