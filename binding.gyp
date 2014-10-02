{
  'variables': {
    'source_root_dir': '<!(python tools/source_root_dir.py)',
    'streamworks_sdk_dir': 'deps/steamworks_sdk'
  },

  'conditions': [
    ['OS=="win"', {
      'variables': {
        'project_name': 'greenworks-win',
        'redist_bin_dir%': '',
        'lib_extension%': 'dll'
      },
    }],
    ['OS=="mac"', {
      'variables': {
        'project_name': 'greenworks-osx',
        'redist_bin_dir%': 'osx32',
        'lib_extension%': 'dylib'
      },
    }],
    ['OS=="linux"', {
      'conditions': [
        ['targets_arch=="ia32"', {
          'variables': {
            'project_name': 'greenworks-linux32',
            'redist_bin_dir%': 'linux32',
            'lib_extension%': 'so'
          }
        }],
        ['targets_arch=="x64"', {
          'variables': {
            'project_name': 'greenworks-linux64',
            'redist_bin_dir%': 'linux64',
            'lib_extension%': 'so'
          }
        }],
      ],
    }],
  ],

  'targets': [
    {
      'target_name': '<(project_name)',
      'sources': [
        'src/greenworks_api.cc',
        'src/greenworks_async_workers.cc',
        'src/greenworks_async_workers.h',
        'src/steam_async_worker.cc',
        'src/steam_async_worker.h',
      ],
      'include_dirs': [
        '<(streamworks_sdk_dir)/public',
        '<!(node -e "require(\'nan\')")'
      ],
      'link_settings': {
        'ldflags': [
          '-L<(source_root_dir)/<(streamworks_sdk_dir)/redistributable_bin/<(redist_bin_dir)'],
        'libraries': [
          '<(source_root_dir)/<(streamworks_sdk_dir)/redistributable_bin/<(redist_bin_dir)/libsteam_api.<(lib_extension)'
        ]
      },
    },
  ]
}