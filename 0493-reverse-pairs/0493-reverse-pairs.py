class Solution(object):

    def mergesort(self, arr,low, high):
        if low >= high:
            return 0
        cnt = 0
        mid = (low + high) // 2
        cnt += self.mergesort(arr, low, mid)
        cnt += self.mergesort(arr, mid+1, high)
        cnt += self.count_pairs(arr, low, mid, high)
        self.merge(arr,low, mid, high)
        return cnt

    
    def merge(self, arr, low , mid, high):
        temp = []
        left = low
        right = mid+1
        while(left <= mid and right <= high):
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1

        arr[low:high + 1] = temp


    def count_pairs(self, arr, low, mid, high):
        cnt = 0
        right = mid + 1
        for i in range(low, mid + 1):
            while(right <= high and arr[i] > 2 * arr[right] ):
                right += 1

            cnt += right - (mid + 1)
        return cnt




    def reversePairs(self, nums):
        return self.mergesort(nums, 0, len(nums)-1 )
    
        