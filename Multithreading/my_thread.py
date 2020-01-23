import threading


def hear_client(nums):
    for i in nums:
        try:
            print("~", i + nums[i])
        except:
            print("~", i)
    return "24123123"

def client_hear(nums):
    a = len(nums)
    for i in nums:
        a-=1
        try:
            print("#", i + nums[a])
        except:
            print("#", i)
    return "asdfasd"

arr = [1, 2, 3, 4, 5]

t1 = threading.Thread(target=hear_client, args=(arr,))
t2 = threading.Thread(target=client_hear, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

