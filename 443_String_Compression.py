class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        length = len(chars)

        write_index = 0
        read_index = 0

        while read_index < length:

            current_char = chars[read_index]
            count = 0

            while read_index < length and chars[read_index] == current_char:
                read_index += 1
                count += 1

            chars[write_index] = current_char
            write_index += 1

            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        return write_index
       


solution = Solution()
def main():
    chars = ["a","a","b","b","c","c","c"]
    print(solution.compress(chars))  # Output: 6, chars = ["a","2","b","2","c","3"]

    chars = ["a"]
    print(solution.compress(chars))  # Output: 1, chars = ["a"]

    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(solution.compress(chars))  # Output: 4, chars = ["a","b","1","2"]

    chars = ["a","a","a","b","b","a","a"]
    print(solution.compress(chars))  # Output: 6, chars = ["a","3","b","2","a","2"]
    chars = ["a","b","c"]
    print(solution.compress(chars))  # Output: 3, chars = ["a","b

if __name__ == "__main__":
    main()    