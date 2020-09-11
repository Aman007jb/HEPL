import numpy as np
def ip_centrality_conversion(ip):
    cent_arr=[]
    for i in ip:
        if 0.00 <= i and i < 1.57:
            cent_arr.append(0.5)
        elif 1.57 <= i and i < 2.22:
            cent_arr.append(1.5)
        elif 2.22 <= i and i < 2.71:
            cent_arr.append(2.5)
        elif 2.71 <= i and i < 3.13:
            cent_arr.append(3.5)
        elif 3.13 <= i and i < 3.50:
            cent_arr.append(4.5)
        elif 3.50 <= i and i < 4.94:
            cent_arr.append(7.5)
        elif 4.94 <= i and i < 6.05:
            cent_arr.append(12.5)
        elif 6.05 <= i and i < 6.98:
            cent_arr.append(17.5)
        elif 6.98 <= i and i < 7.81:
            cent_arr.append(22.5)
        elif 7.81 <= i and i < 8.55:
            cent_arr.append(27.5)
        elif 8.55 <= i and i < 9.23:
            cent_arr.append(32.5)
        elif 9.23 <= i and i < 9.88:
            cent_arr.append(37.5)
        elif 9.88 <= i and i < 10.47:
            cent_arr.append(42.5)
        elif 10.47 <= i and i < 11.04:
            cent_arr.append(47.5)
        elif 11.04 <= i and i < 11.58:
            cent_arr.append(52.5)
        elif 11.58 <= i and i < 12.09:
            cent_arr.append(57.5)
        elif 12.09 <= i and i < 12.58:
            cent_arr.append(62.5)
        elif 12.58 <= i and i < 13.05:
            cent_arr.append(67.5)
        elif 13.05 <= i and i < 13.52:
            cent_arr.append(72.5)
        elif 13.52 <= i and i < 13.97:
            cent_arr.append(77.5)
        elif 13.97 <= i and i < 14.43:
            cent_arr.append(82.5)
        elif 14.43 <= i and i < 14.96:
            cent_arr.append(87.5)
        elif 14.96 <= i and i < 15.67:
            cent_arr.append(92.5)
        elif 15.67 <= i and i < 20.00:
            cent_arr.append(97.5)
    
    
    cent_arr = np.array(cent_arr)
    return cent_arr