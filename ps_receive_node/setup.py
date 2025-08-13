from setuptools import find_packages, setup

package_name = 'ps_receive_node'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools',
                      'mnist_cnn_interface',
                      'rclpy',
                      ],
    zip_safe=False,
    maintainer='lzh',
    maintainer_email='zhihui.lin134@gmail.com',
    description='receive node for mnist_cnn digit recognition',
    license='Apache-2.0',
    tests_require=['pytest','launch_testing', 'launch_testing_ros'],
    entry_points={
        'console_scripts': [
        'receive = ps_receive_node.receive:main'
        ],
    },
)
