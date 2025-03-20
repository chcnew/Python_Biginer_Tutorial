# _*_encoding: utf-8 _*_

# import subprocess
#
# p1 = subprocess.Popen(
#     "python -B -c \"print('show')\"",
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE,
#     shell=True
# )
#
# for out in iter(p1.stdout.readline, b""):
#     print("out:{}".format(str(out, encoding="utf-8")), "err:{}".format(p1.stdout.readline()))
#
# p2 = subprocess.Popen(
#     "python -B -c \"print('me')\"",
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE,
#     shell=True
# )
#
# out, err = p2.communicate()
# print("out:{}".format(str(out, encoding="utf-8")), f"err:{err}")

x = "饕餮"
y = x.encode("utf-16")
print(type(y))
try:
    z = y.decode("utf-8")
except UnicodeDecodeError as e:
    z = y.decode("utf-16")

print("z={}".format(z))
