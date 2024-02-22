all_3d_arr = []
def save_3d_arrray(x, y, z):
    for i in range(x):
        for j in range(y):
            for k in range(z):
                all_3d_arr.append([i,j,k])

# def get_res_arr(n):
    

def get_result_array(x, y, z, n):
    save_3d_arrray(x+1,y+1,z+1)
    print(all_3d_arr)
    # result = get_res_arr(n)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    get_result_array(x, y, z, n)
    