
# #include<iostream>
# #define MAX 20
# using namespace std;
 
# int n;
# int Bool[MAX] = { 0 };//Đánh dấu chưa có phần tử nào sử dụng hết
# int A[MAX];//Lưu hoán vị vào mảng A
 
# void xuat() {
#     for (int i = 1; i <= n; i++)
#         cout << A[i] << " ";
#     cout << endl;
# }
 
# void Try(int k) {
#     for (int i = 1; i <= n; i++) {
#         //Kiểm tra nếu phần tử chưa được chọn thì sẽ đánh dấu
#         if (!Bool[i]) {
#             A[k] = i; // Lưu một phần tử vào hoán vị
#             Bool[i] = 1;//Đánh dấu đã dùng
#             if (k == n)//Kiểm tra nếu đã chứa một hoán vị thì xuất
#                 xuat();
#             else
#                 Try(k + 1);
#             Bool[i] = 0;
#         }
#     }
# }
n = 3
Bool = [None]*(n+1)
a = [None]*(n+1)
result = []


def Try(k):
    global n
    global Bool
    global a
    global result
    for i in range(1,n+1):
        print('Bool[i] ',Bool[i])
        if Bool[i] == None:
            a[k] = i 
            Bool[i] = 1

            valid = True
            for j in range(1,len(a)):
                if a[j] == None:
                    valid = False

            if valid == True:  
                result.append(a)
            else:
                Try(k+1)
            Bool[i] = None

Try(1)
print(result)

# int main() {
#     cout << "Mhap n: ";
#     cin >> n;
#     Try(1);
# }