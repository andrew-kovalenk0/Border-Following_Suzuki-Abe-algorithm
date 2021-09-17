import numpy as np
import time
import cv2


def find_clockwise(borders, center, i2j2):
    i = i2j2[0]
    j = i2j2[1]
    if center[0] - i == 0 and center[1] - j == -1:
        if borders[i+1, j] != 0:
            return [i+1, j]
        if borders[i+1, j-1] != 0:
            return [i+1, j-1]
        if borders[i+1, j-2] != 0:
            return [i+1, j-2]
        if borders[i, j-2] != 0:
            return [i, j-2]
        if borders[i-1, j-2] != 0:
            return [i-1, j-2]
        if borders[i-1, j-1] != 0:
            return [i-1, j-1]
        if borders[i-1, j] != 0:
            return [i-1, j]

    if center[0] - i == 1 and center[1] - j == -1:
        if borders[i+1, j] != 0:
            return [i+1, j]
        if borders[i+2, j] != 0:
            return [i+2, j]
        if borders[i+2, j-1] != 0:
            return [i+2, j-1]
        if borders[i+2, j-2] != 0:
            return [i+2, j-2]
        if borders[i+1, j-2] != 0:
            return [i+1, j-2]
        if borders[i, j-2] != 0:
            return [i, j-2]
        if borders[i, j-1] != 0:
            return [i, j-1]

    if center[0] - i == 1 and center[1] - j == 0:
        if borders[i, j+1] != 0:
            return [i, j+1]
        if borders[i+1, j+1] != 0:
            return [i+1, j+1]
        if borders[i+2, j+1] != 0:
            return [i+2, j+1]
        if borders[i+2, j] != 0:
            return [i+2, j]
        if borders[i+2, j-1] != 0:
            return [i+2, j-1]
        if borders[i+1, j-1] != 0:
            return [i+1, j-1]
        if borders[i, j-1] != 0:
            return [i, j-1]

    if center[0] - i == 1 and center[1] - j == 1:
        if borders[i, j+1] != 0:
            return [i, j+1]
        if borders[i, j+2] != 0:
            return [i, j+2]
        if borders[i+1, j+2] != 0:
            return [i+1, j+2]
        if borders[i+2, j+2] != 0:
            return [i+2, j+2]
        if borders[i+2, j+1] != 0:
            return [i+2, j+1]
        if borders[i+2, j] != 0:
            return [i+2, j]
        if borders[i+1, j] != 0:
            return [i+1, j]

    if center[0] - i == 0 and center[1] - j == 1:
        if borders[i-1, j] != 0:
            return [i-1, j]
        if borders[i-1, j+1] != 0:
            return [i-1, j+1]
        if borders[i-1, j+2] != 0:
            return [i-1, j+2]
        if borders[i, j+2] != 0:
            return [i, j+2]
        if borders[i+1, j+2] != 0:
            return [i+1, j+2]
        if borders[i+1, j+1] != 0:
            return [i+1, j+1]
        if borders[i+1, j] != 0:
            return [i+1, j]

    if center[0] - i == -1 and center[1] - j == 1:
        if borders[i, j+1] != 0:
            return [i, j+1]
        if borders[i, j+2] != 0:
            return [i, j+2]
        if borders[i-1, j+2] != 0:
            return [i-1, j+2]
        if borders[i-2, j+2] != 0:
            return [i-2, j+2]
        if borders[i-2, j+1] != 0:
            return [i-2, j+1]
        if borders[i-2, j] != 0:
            return [i-2, j]
        if borders[i-1, j] != 0:
            return [i-1, j]

    if center[0] - i == -1 and center[1] - j == 0:
        if borders[i, j-1] != 0:
            return [i, j-1]
        if borders[i-1, j-1] != 0:
            return [i-1, j-1]
        if borders[i-2, j-1] != 0:
            return [i-2, j-1]
        if borders[i-2, j] != 0:
            return [i-2, j]
        if borders[i-2, j+1] != 0:
            return [i-2, j+1]
        if borders[i-1, j+1] != 0:
            return [i-1, j+1]
        if borders[i, j+1] != 0:
            return [i, j+1]

    if center[0] - i == -1 and center[1] - j == -1:
        if borders[i, j-1] != 0:
            return [i, j-1]
        if borders[i, j-2] != 0:
            return [i, j-2]
        if borders[i-1, j-2] != 0:
            return [i-1, j-2]
        if borders[i-2, j-2] != 0:
            return [i-2, j-2]
        if borders[i-2, j-1] != 0:
            return [i-2, j-1]
        if borders[i-2, j] != 0:
            return [i-2, j]
        if borders[i-1, j] != 0:
            return [i-1, j]
    return None


def find_counterclockwise(borders, center, i2j2):
    i = i2j2[0]
    j = i2j2[1]
    exam_pixels = [[]]
    if center[0] - i == 0 and center[1] - j == -1:
        if borders[i-1, j] != 0:
            return [i-1, j], exam_pixels
        else:
            exam_pixels.append([i-1, j])
        if borders[i-1, j-1] != 0:
            return [i-1, j-1], exam_pixels
        else:
            exam_pixels.append([i-1, j-1])
        if borders[i-1, j-2] != 0:
            return [i-1, j-2], exam_pixels
        else:
            exam_pixels.append([i-1, j-2])
        if borders[i, j-2] != 0:
            return [i, j-2], exam_pixels
        else:
            exam_pixels.append([i, j-1])
        if borders[i+1, j-2] != 0:
            return [i+1, j-2], exam_pixels
        else:
            exam_pixels.append([i+1, j-2])
        if borders[i+1, j-1] != 0:
            return [i+1, j-1], exam_pixels
        else:
            exam_pixels.append([i+1, j-1])
        if borders[i+1, j] != 0:
            return [i+1, j], exam_pixels
        else:
            exam_pixels.append([i+1, j])

    if center[0] - i == 1 and center[1] - j == -1:
        if borders[i, j-1] != 0:
            return [i, j-1], exam_pixels
        else:
            exam_pixels.append([i, j-1])
        if borders[i, j-2] != 0:
            return [i, j-2], exam_pixels
        else:
            exam_pixels.append([i, j-2])
        if borders[i+1, j-2] != 0:
            return [i+1, j-2], exam_pixels
        else:
            exam_pixels.append([i+1, j-2])
        if borders[i+2, j-2] != 0:
            return [i+2, j-2], exam_pixels
        else:
            exam_pixels.append([i+2, j-2])
        if borders[i+2, j-1] != 0:
            return [i+2, j-1], exam_pixels
        else:
            exam_pixels.append([i+2, j-1])
        if borders[i+2, j] != 0:
            return [i+2, j], exam_pixels
        else:
            exam_pixels.append([i+2, j])
        if borders[i+1, j] != 0:
            return [i+1, j], exam_pixels
        else:
            exam_pixels.append([i+1, j])

    if center[0] - i == 1 and center[1] - j == 0:
        if borders[i, j-1] != 0:
            return [i, j-1], exam_pixels
        else:
            exam_pixels.append([i, j-1])
        if borders[i+1, j-1] != 0:
            return [i+1, j-1], exam_pixels
        else:
            exam_pixels.append([i+1, j-1])
        if borders[i+2, j-1] != 0:
            return [i+2, j-1], exam_pixels
        else:
            exam_pixels.append([i+2, j-1])
        if borders[i+2, j] != 0:
            return [i+2, j], exam_pixels
        else:
            exam_pixels.append([i+2, j])
        if borders[i+2, j+1] != 0:
            return [i+2, j+1], exam_pixels
        else:
            exam_pixels.append([i+2, j+1])
        if borders[i+1, j+1] != 0:
            return [i+1, j+1], exam_pixels
        else:
            exam_pixels.append([i+1, j+1])
        if borders[i, j+1] != 0:
            return [i, j+1], exam_pixels
        else:
            exam_pixels.append([i, j+1])

    if center[0] - i == 1 and center[1] - j == 1:
        if borders[i+1, j] != 0:
            return [i+1, j], exam_pixels
        else:
            exam_pixels.append([i+1, j])
        if borders[i+2, j] != 0:
            return [i+2, j], exam_pixels
        else:
            exam_pixels.append([i+2, j])
        if borders[i+2, j+1] != 0:
            return [i+2, j+1], exam_pixels
        else:
            exam_pixels.append([i+2, j+1])
        if borders[i+2, j+2] != 0:
            return [i+2, j+2], exam_pixels
        else:
            exam_pixels.append([i+2, j+2])
        if borders[i+1, j+2] != 0:
            return [i+1, j+2], exam_pixels
        else:
            exam_pixels.append([i+1, j+2])
        if borders[i, j+2] != 0:
            return [i, j+2], exam_pixels
        else:
            exam_pixels.append([i, j+2])
        if borders[i, j+1] != 0:
            return [i, j+1], exam_pixels
        else:
            exam_pixels.append([i, j+1])

    if center[0] - i == 0 and center[1] - j == 1:
        if borders[i+1, j] != 0:
            return [i+1, j], exam_pixels
        else:
            exam_pixels.append([i+1, j])
        if borders[i+1, j+1] != 0:
            return [i+1, j+1], exam_pixels
        else:
            exam_pixels.append([i+1, j+1])
        if borders[i+1, j+2] != 0:
            return [i+1, j+2], exam_pixels
        else:
            exam_pixels.append([i+1, j+2])
        if borders[i, j+2] != 0:
            return [i, j+2], exam_pixels
        else:
            exam_pixels.append([i, j+2])
        if borders[i-1, j+2] != 0:
            return [i-1, j+2], exam_pixels
        else:
            exam_pixels.append([i-1, j+2])
        if borders[i-1, j+1] != 0:
            return [i-1, j+1], exam_pixels
        else:
            exam_pixels.append([i-1, j+1])
        if borders[i-1, j] != 0:
            return [i-1, j], exam_pixels
        else:
            exam_pixels.append([i-1, j])

    if center[0] - i == -1 and center[1] - j == 1:
        if borders[i, j+1] != 0:
            return [i, j+1], exam_pixels
        else:
            exam_pixels.append([i, j+1])
        if borders[i, j+2] != 0:
            return [i, j+2], exam_pixels
        else:
            exam_pixels.append([i, j+2])
        if borders[i-1, j+2] != 0:
            return [i-1, j+2], exam_pixels
        else:
            exam_pixels.append([i-1, j+2])
        if borders[i-2, j+2] != 0:
            return [i-2, j+2], exam_pixels
        else:
            exam_pixels.append([i-2, j+2])
        if borders[i-2, j+1] != 0:
            return [i-2, j+1], exam_pixels
        else:
            exam_pixels.append([i-2, j+1])
        if borders[i-2, j] != 0:
            return [i-2, j], exam_pixels
        else:
            exam_pixels.append([i-2, j])
        if borders[i-1, j] != 0:
            return [i-1, j], exam_pixels
        else:
            exam_pixels.append([i-1, j])

    if center[0] - i == -1 and center[1] - j == 0:
        if borders[i, j+1] != 0:
            return [i, j+1], exam_pixels
        else:
            exam_pixels.append([i, j+1])
        if borders[i-1, j+1] != 0:
            return [i-1, j+1], exam_pixels
        else:
            exam_pixels.append([i-1, j+1])
        if borders[i-2, j+1] != 0:
            return [i-2, j+1], exam_pixels
        else:
            exam_pixels.append([i-2, j+1])
        if borders[i-2, j] != 0:
            return [i-2, j], exam_pixels
        else:
            exam_pixels.append([i-2, j])
        if borders[i-2, j-1] != 0:
            return [i-2, j-1], exam_pixels
        else:
            exam_pixels.append([i-2, j-1])
        if borders[i-1, j-1] != 0:
            return [i-1, j-1], exam_pixels
        else:
            exam_pixels.append([i-1, j-1])
        if borders[i, j-1] != 0:
            return [i, j-1], exam_pixels
        else:
            exam_pixels.append([i, j-1])

    if center[0] - i == -1 and center[1] - j == -1:
        if borders[i-1, j] != 0:
            return [i-1, j], exam_pixels
        else:
            exam_pixels.append([i-1, j])
        if borders[i-2, j] != 0:
            return [i-2, j], exam_pixels
        else:
            exam_pixels.append([i-2, j])
        if borders[i-2, j-1] != 0:
            return [i-2, j-1], exam_pixels
        else:
            exam_pixels.append([i-2, j-1])
        if borders[i-2, j-2] != 0:
            return [i-2, j-2], exam_pixels
        else:
            exam_pixels.append([i-2, j-2])
        if borders[i-1, j-2] != 0:
            return [i-1, j-2], exam_pixels
        else:
            exam_pixels.append([i-1, j-2])
        if borders[i, j-2] != 0:
            return [i, j-2], exam_pixels
        else:
            exam_pixels.append([i, j-2])
        if borders[i, j-1] != 0:
            return [i, j-1], exam_pixels
        else:
            exam_pixels.append([i, j-1])
    return None, exam_pixels


def find_borders(img):
    nbd = 1
    borders = np.array(img, dtype=int)
    borders[borders == 255] = 1
    for i in range(borders.shape[0]):
        lnbd = 1
        for j in range(borders.shape[1]):
            if borders[i, j] != 0:

                # Step 1, outer border
                if borders[i, j] == 1 and borders[i, j-1] == 0:
                    nbd += 1
                    i2j2 = [i, j-1]
                    # Step 3.1
                    i1j1 = find_clockwise(borders, [i, j], i2j2)
                    if i1j1:
                        # Step 3.2
                        i2j2 = i1j1
                        i3j3 = [i, j]
                        # Step 3.3
                        while True:
                            i4j4, exam_pixels = find_counterclockwise(borders, i3j3, i2j2)
                            # Step 3.4
                            if [i3j3[0], i3j3[1] + 1] in exam_pixels:
                                borders[i3j3[0], i3j3[1]] = -nbd
                            if [i3j3[0], i3j3[1] + 1] not in exam_pixels and borders[i3j3[0], i3j3[1]] == 1:
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
                    if img[i, j] > 1:
                        lnbd = img[i, j]
                    # Step 3.1
                    i1j1 = find_clockwise(borders, [i, j], i2j2)
                    if i1j1:
                        # Step 3.2
                        i2j2 = i1j1
                        i3j3 = [i, j]
                        # Step 3.3
                        while True:
                            i4j4, exam_pixels = find_counterclockwise(borders, i3j3, i2j2)
                            # Step 3.4
                            if [i3j3[0], i3j3[1] + 1] in exam_pixels:
                                borders[i3j3[0], i3j3[1]] = -nbd
                            if [i3j3[0], i3j3[1] + 1] not in exam_pixels and borders[i3j3[0], i3j3[1]] == 1:
                                borders[i3j3[0], i3j3[1]] = nbd
                            # Step 3.5
                            if i4j4 == [i, j] and i3j3 == i1j1:
                                break
                            else:
                                i2j2 = i3j3
                                i3j3 = i4j4
                    else:
                        borders[i, j] = -nbd

                # Step 1, Resume raster scan
                else:
                    # Step 4
                    if borders[i, j] != 1:
                        lnbd = borders[i, j]
    return borders, nbd


if __name__ == '__main__':
    start_time = time.time()
    image = cv2.imread('image_3.png', 0)
    border, num = find_borders(image)
    np.savetxt('border.txt', border, fmt='%d')
    border[border < 0] *= -1
    border[border > 1] *= int(255 / num)
    cv2.imwrite('border.png', border)
    print(f'{time.time() - start_time} seconds')
