class HttpRequest(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def func1():
        print("HttpRequest.func1")

    @staticmethod
    def func2():
        print("HttpRequest.func2")


class DrfRequest(object):
    def __init__(self, request, d, e, f):
        self._request = request
        self.d = d
        self.e = e
        self.f = f

    def __getattr__(self, item):
        try:
            result = getattr(self._request, item)
        except AttributeError:
            result = self.__getattribute__(item)
        return result


if __name__ == '__main__':
    http_request = HttpRequest(1, 2, 3)
    drf_request = DrfRequest(http_request, 4, 5, 6)
    drf_request.func1()
    drf_request.func2()
    drf_request.func3()
