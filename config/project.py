project_github_username = 'veltzer'
project_name = 'pydmt'
project_website = 'https://{project_github_username}.github.io/{project_name}'.format(**locals())
project_website_source = 'https://github.com/{project_github_username}/{project_name}'.format(**locals())
project_website_git = 'git://github.com/{project_github_username}/{project_name}.git'.format(**locals())
project_website_download_ppa = 'https://launchpanet/~mark-veltzer/+archive/ubuntu/ppa'
project_website_download_src = project_website_source
# project_paypal_donate_button_id='ASPRXR59H2NTQ'
# project_google_analytics_tracking_id='UA-56436979-1'
project_long_description = 'python dependency management tool'
project_short_description = 'python dependency management tool'
# keywords to put on html pages or for search, dont put the name of the project or my details
# as they will be added automatically...
project_keywords = [
    'pydmt',
    'cons',
    'scons',
    'software construction',
    'make',
    'maven',
    'mvn',
]
project_license = 'MIT'
project_year_started = '2016'
project_description = 'python dependency management tool'
project_platforms = [
    'python3',
]
project_classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Utilities',
]
project_data_files = []
# project_data_files.append(templar.utils.hlp_files_under('/usr/bin', 'src/*'))
