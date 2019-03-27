from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()
    setup(
        name='spotifyWeeklyEDM',
        version='0.1.0',
        author='Joey Engel',
        author_email='joeyengel@pm.me',
        description='A utility that creates weekly Spotify playlists scraped from reddit.com/r/EDM',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/your_username/pgbackup',
        packages=find_packages('src')
    )
