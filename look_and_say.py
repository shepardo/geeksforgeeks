# Look and say in Python 3

def look_and_say(idx, my_callback):
    s = '1'
    while idx > 0:
        my_callback(s)
        idx -= 1
        new_s = ''
        prev_c = ''
        cnt_prev = 0
        for c in s:
            if prev_c != c:
                if cnt_prev != 0:
                    chunk_s = "{0}{1}".format(str(cnt_prev), prev_c)
                    new_s = new_s + chunk_s
                cnt_prev = 1
                prev_c = c
            else:
                cnt_prev += 1
        if cnt_prev != 0:
            chunk_s = "{0}{1}".format(str(cnt_prev), prev_c)
            new_s = new_s + chunk_s
        s = new_s

def my_print(s):
    print(s)

if __name__ == "__main__":
    look_and_say(20, my_print)
