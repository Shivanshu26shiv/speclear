import setuptools

with open("README", "r") as fh:
    ld = fh.read()

setuptools.setup(
  name = 'speclear',         # How you named your package folder (MyLib)
  packages = ['speclear'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'speclear - delete specific history in all 4 major windows browsers',
  long_description = ld,
  long_description_content_type="text/markdown",
  # Give a short description about your library
  author = 'Shivanshu Srivastava',                   # Type in your name
  author_email = 'shivanshu26shiv@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Shivanshu26shiv/speclear',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Shivanshu26shiv/speclear/archive/v_02.4.2.tar.gz',    # I explain this later on
  keywords = ['browser', 'browser history', 'chrome', 'firefox', 'opera', 'safari', 'ie'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'Operating System :: Microsoft :: Windows',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    # 'Programming Language :: Python :: 2.7',
    # 'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ]
)
