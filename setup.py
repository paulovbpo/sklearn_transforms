from setuptools import setup


setup(
      name='my_custom_sklearn_transforms_1',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/paulovbpo/sklearn_transforms/',
      author='Paulo Victor Oliveira',
      author_email='paulovbpo@hotmail.com',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms_1'
      ],
      zip_safe=False
)
