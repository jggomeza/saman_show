import itertools as it

class Vampire():
    def get_fangs(self, num_str):
        num_iter = it.permutations(num_str, len(num_str))
        for num_list in num_iter:
            v = ''.join(num_list)
            x, y = v[:int(len(v)/2)], v[int(len(v)/2):]
            if x[-1] == '0' and y[-1] == '0':
                continue
            if int(x) * int(y) == int(num_str):
                return x,y
        return False

    def is_vampire(self, m_int):
        n_str = str(m_int)
        if len(n_str) % 2 == 1:
            return False
        fangs = self.get_fangs(n_str)
        if not fangs:
            return False
        return True

# for test_num in range(150000):
#     if is_vampire(test_num):
#         print ("{}".format(test_num), end = ", ")
van = Vampire()
# print(van.is_vampire(1260))