from setuptools import setup, find_packages
setup(
    name="demo",
    version="1.0",
    packages = find_packages('src'),  # 包含所有src中的包
    package_dir = {'':'src'},   # 告诉distutils包都在src下

    package_data = {
        # 任何包中含有.txt文件，都包含它
        '': ['*.txt'],
        # 包含demo包data文件夹中的 *.dat文件
        'demo': ['data/*.dat'],
    }

)
