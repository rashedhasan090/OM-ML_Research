import shutil

src = r'Sol_Abs_Gen.py'
ext = r'.py'

#Change the 5 to what number you want to duplicate
for i in range(1000):
    shutil.copy(src, f'{src + str(i) + ext}')
